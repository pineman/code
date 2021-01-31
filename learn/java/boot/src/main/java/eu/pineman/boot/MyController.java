package eu.pineman.boot;

import org.springframework.http.HttpStatus;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

@RestController
public class MyController {

    @GetMapping("/")
    public Flux<String> getHello(ServerHttpResponse response) {
        response.setStatusCode(HttpStatus.FOUND);
        return Flux.just("Hello!\n");
    }

}
