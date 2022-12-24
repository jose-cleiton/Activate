package main

import "fmt"

type DivideActivities struct {
	durations      []float64
	hoursPerDay float64
}

func (d *DivideActivities) findBestOption(dayTotal float64, remainingDurations []float64) float64 {
	for _, duration := range remainingDurations {
		if d.hoursPerDay - (dayTotal + duration) >= 0 {
			return duration
		}
	}
	return 0
}

func (d *DivideActivities) findMinimumDays() [][]float64 {
	days := make([][]float64, 1)
	days[0] = []float64{d.durations[0]}
	remainingDurations := d.durations[1:]
	dayTotal := d.durations[0]

	for len(remainingDurations) > 0 {
		option := d.findBestOption(dayTotal, remainingDurations)
		if option > 0 {
			days[len(days)-1] = append(days[len(days)-1], option)
			dayTotal += option
			remainingDurations = remainingDurations[1:]
		} else {
			days = append(days, []float64{})
			dayTotal = 0
		}
	}

	return days
}


func main() {
	durations := []float64{1.90, 1.25, 2.5, 1.75, 1.04}
	hoursPerDay := 3.0

	divideActivities := &DivideActivities{durations, hoursPerDay}
	days := divideActivities.findMinimumDays()

	for i, day := range days {
		fmt.Printf("Day %d: %v\n", i+1, day)
	}
	fmt.Printf("Total days: %d\n", len(days))
}
