from flask import Flask, json, jsonify, request, make_response
import uuid
import redis
app = Flask(__name__)
redis_host = "redis-service.knative-samples.svc.cluster.local"  # Replace with the correct DNS name of your Redis service
redis_port = 6379
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
@app.route('/', methods=['POST'])
def hello_world():
    app.logger.warning(request.data)
    # Respond with another event (optional)
    response = make_response({
        "msg": "Hi from helloworld-python app!"
    })
    response.headers["Ce-Id"] = str(uuid.uuid4())
    response.headers["Ce-specversion"] = "0.3"
    response.headers["Ce-Source"] = "knative/eventing/samples/hello-world"
    response.headers["Ce-Type"] = "dev.knative.samples.hifromknative"
    try:
        cdata = request.get_data()
        data_dict = json.loads(cdata)
        cmd = data_dict.get('cmd')
        if cmd == "POST":
           data = request.json
           key = data.get('key')
           value = data.get('value')
           value = json.dumps(value)
        # Insert JSON data into Redis
           redis_client.set(key, value)
           return response
        elif cmd == "PUT":
            data = request.json
            key = data.get('key')
            value = data.get('value')
            # Update JSON data in Redis
            if redis_client.exists(key):
               value = json.dumps(value) 
               redis_client.set(key, value)
               return response
            else:
               return response
        elif cmd == "DELETE":
             data = request.json
             key = data.get('key')
             if redis_client.exists(key):
                redis_client.delete(key)
                return response
        else:
             return response
    except:
        return response
    finally:
        return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)