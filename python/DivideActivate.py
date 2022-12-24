class DivideActivities:
    def __init__(self, durations, hours_per_day):
        self.durations = durations
        self.hours_per_day = hours_per_day

    def find_best_option(self, day_total, remaining_durations):
        best_option = next(
            (
                duration
                for duration in remaining_durations
                if self.hours_per_day - (day_total + duration) >= 0
            ),
            None,
        )
        if best_option:
            return best_option
        return None

    def find_minimum_days(self):

        days = [[self.durations[0]]]
        remaining_durations = self.durations[1:]
        day_total = self.durations[0]

        while remaining_durations:
            option = self.find_best_option(day_total, remaining_durations)
            if option:
                days[-1].append(option)
                day_total += option
                remaining_durations = [
                    duration
                    for duration in remaining_durations
                    if duration != option
                ]
            else:
                days.append([])
                day_total = 0

        return days


if __name__ == "__main__":
    durations = [1.90, 1.25, 2.5, 1.75, 1.04]
    hours_per_day = 3

    divide_activities = DivideActivities(durations, hours_per_day)
    daysTotal = divide_activities.find_minimum_days()

    for index, day in enumerate(daysTotal):
        print("{} Dia {}".format(index + 1, day))
        print("Total de dias: {}".format(len(daysTotal)))
