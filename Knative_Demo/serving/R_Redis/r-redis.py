from flask import Flask, json, jsonify, request, make_response
import uuid
import redis
import os
app = Flask(__name__)
redis_host = "redis-service.knative-samples.svc.cluster.local"  # Replace with the correct DNS name of your Redis service
redis_port = 6379
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
@app.route('/read/<int:key>',methods=['GET'])
def Read(key):
    try:
        # Read the JSON data from Redis based on the integer key
        value = redis_client.get(key)
        if value is None:
            return jsonify({"error": "Item not found"}), 404
        return jsonify({"key": key, "value": value.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))