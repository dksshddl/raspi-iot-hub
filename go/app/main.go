package main

import (
	"fmt"

	"github.com/dksshddl/raspi-iot-hub/app/sensor"
)

func main() {
	sensor.Read()
	fmt.Println("hello world")
}
