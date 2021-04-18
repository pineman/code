SRC=$(shell find . -type f -name "*.go")
all: $(SRC:%.go=%)

%: %.go
	go build -o $(GOPATH)/bin/$(notdir $@) $@.go

clean:
	rm -rf $(addprefix $(GOPATH)/bin/, $(notdir $(SRC:./%.go=%)))
