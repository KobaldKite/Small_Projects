import argparse


TYPE = {
    'SILVER': 1,
    'GOLD': 2
}

TURN_SHIFT = -1


def parse_direction(direction):
    return {
        '>': [0, 1],
        '<': [0, -1],
        '^': [1, 0],
        'v': [-1, 0]
    }[direction]  # TODO: Use 'get' here with some  default values


class Santa(object):
    def __init__(self):
        self.location = (0, 0)
        self.deliveries = [(0, 0), ]

    def move(self, direction):
        self.location = tuple([sum(coordinates) for coordinates in zip(self.location, direction)])
        self.deliveries.append(self.location)


class DeliveryPlan(object):
    def __init__(self, args):
        self.file_path = args.file_path
        self.santa_count = TYPE[args.task_type]
        with open(args.file_path, 'r') as input_file:
            self.directions = input_file.read().strip("\n")

    def santa_job(self):
        santas = [Santa() for count in xrange(self.santa_count)]
        turn = 0
        for direction in self.directions:
            santas[turn].move(parse_direction(direction))
            if turn == self.santa_count + TURN_SHIFT:
                turn = 0
            else:
                turn += 1
        delivery_coverage = [delivery for santa in santas for delivery in santa.deliveries]
        delivery_count = len(set(delivery_coverage))
        print delivery_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_path')
    parser.add_argument('-t', action='store', dest='task_type', default='SILVER')
    args = parser.parse_args()
    delivery_plan = DeliveryPlan(args)
    delivery_plan.santa_job()


if __name__ == '__main__':  # TESTED AND WORKS
    main()
