package main

import (
	"fmt"
	"time"

	"github.com/stianeikeland/go-rpio"
)

func main() {
	fmt.Println("Hello world")
	err := rpio.Open()
	if err != nil {
		panic(err)
	}

	pin := rpio.Pin(2)
	pin.Input()
	for {
		res := pin.Read()
		fmt.Println(res)
		time.Sleep(1 * 1000)
	}
}
