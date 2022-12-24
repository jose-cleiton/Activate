class DivideActivities {
  constructor(durations, hoursPerDay) {
    this.durations = durations;
    this.hoursPerDay = hoursPerDay;
  }

  findBestOption(dayTotal, remainingDurations) {
    const bestOption = remainingDurations.find(duration => this.hoursPerDay - (dayTotal + duration) >= 0);
    if (bestOption) {
      return bestOption;
    }
    return null;
  }

  findMinimumDays() {
    const days = [[this.durations[0]]];
    let remainingDurations = this.durations.slice(1);
    let dayTotal = this.durations[0];

    while (remainingDurations.length > 0) {
      const option = this.findBestOption(dayTotal, remainingDurations);
      if (option) {
        days[days.length - 1].push(option);
        dayTotal += option;
        remainingDurations = remainingDurations.filter(duration => duration !== option);
      } else {
        days.push([]);
        dayTotal = 0;
      }
    }

    return days;
  }
}

const divideActivities = new DivideActivities([1.90, 1.25, 2.5, 1.75, 1.04], 3);
const result = divideActivities.findMinimumDays();
result.forEach((day, i) => console.log(`Day ${i + 1}: ${day}`));
console.log(`Total days: ${result.length}`);
