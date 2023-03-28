package main

import (
	"encoding/json"
	"log"
	"math/rand"

	maelstrom "github.com/jepsen-io/maelstrom/demo/go"
)

func main() {
	n := maelstrom.NewNode()
	n.Handle("generate", func(msg maelstrom.Message) error {
		var body map[string]any
		if err := json.Unmarshal(msg.Body, &body); err != nil {
			return err
		}
		body["type"] = "generate_ok"
		// Realistically though would probably either use /dev/urandom directly,
		// maybe concatenated with ns precision clock, or you know just a UUID
		// library or something like https://en.wikipedia.org/wiki/Snowflake_ID
		// As of go 1.20, it's automatically seeded
		// https://tip.golang.org/doc/go1.20#math/rand
		body["id"] = rand.Float64()
		return n.Reply(msg, body)
	})
	if err := n.Run(); err != nil {
		log.Fatal(err)
	}
}
