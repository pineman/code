SRC=$(shell find . -type f -name "*.go")
all: $(SRC:%.go=%)

%: %.go
	go build -o $(GOPATH)/bin/$@ $@.go

clean:
	rm -rf $(addprefix $(GOPATH)/bin/, $(SRC:./%.go=%))
