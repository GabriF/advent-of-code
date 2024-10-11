package aoc

import (
	"os"
	"bufio"
)

func LeggiInput(nomeFile string) ([]string, bool) {
	f, err := os.Open(nomeFile)
	if err != nil {
		return nil, false
	}
	r := bufio.NewScanner(f)

	righe := []string{}
	for r.Scan() {
		linea := r.Text()
		righe = append(righe, linea)

	}

	return righe, true
}
