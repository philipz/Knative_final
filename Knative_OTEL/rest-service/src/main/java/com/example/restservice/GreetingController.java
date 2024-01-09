package com.example.restservice;

import java.util.concurrent.atomic.AtomicLong;
import org.springframework.web.client.RestTemplate;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
public class GreetingController {

	private static final String template_member = "Hello, dear Member %s!";
	private static final String template_anonymous = "Hello, %s, Please fee free to register!";
	private final AtomicLong counter = new AtomicLong();

	
	private static final Logger logger = LoggerFactory.getLogger(GreetingController.class);

	@GetMapping("/greeting")
	public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
		
		String url = String.format("http://service-person.elb.svc.cluster.local/person?name=%s", name);
		logger.info(String.format("restTemplate url: %s", url));
		RestTemplate restTemplate = new RestTemplate();
		String result = restTemplate.getForObject(url, String.class);
			
		if (result.equals("true")){
			logger.info(String.format("The person %s is a member.", name));
			return new Greeting(counter.incrementAndGet(), String.format(template_member, name));
		}else{
			logger.info(String.format("The person %s is NOT a member, recommend to register.", name));
			return new Greeting(counter.incrementAndGet(), String.format(template_anonymous, name));
		} 
		
	}
}