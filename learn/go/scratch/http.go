package main

import (
	"fmt"
	"io"
	"net/http"
	"time"
)

func slowHandler(w http.ResponseWriter, req *http.Request) {
	time.Sleep(2 * time.Second)
	io.WriteString(w, "I am slow!\n")
}

func mainHTTP() {
	srv := http.Server{
		Addr:         "localhost:8888",
		WriteTimeout: 5 * time.Second,
		Handler:      http.TimeoutHandler(http.HandlerFunc(slowHandler), 1*time.Second, "Timeout!"),
	}
	err := srv.ListenAndServe()
	if err != nil {
		fmt.Printf("Server failed: %s\n", err)
	}
}
