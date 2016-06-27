import argparse


TYPE = {
    'SILVER': 1,
    'GOLD': 2
}

TURN_SHIFT = -1

PARSE_INSTRUCTIONS = {
    '>': [0, 1],
    '<': [0, -1],
    '^': [1, 0],
    'v': [-1, 0]
}


def parse_direction(direction):
    """
    :param direction: a symbol, > v ^ < for moving in one of four directions
    :return: increase in coordinates, two-dimensional vector, [x, y]
    If the given direction is an incorrect symbol, Santa doesn't move,
    but the turn is given to the next Santa
    """
    if direction not in PARSE_INSTRUCTIONS.values():
        print 'Some directions are in a wrong format.\
               Such directions will be ignored.'
    return PARSE_INSTRUCTIONS.get(direction, [0, 0])


class Santa(object):
    """
    Santa knows where he is and what deliveries he has made.
    He can move, automatically adding the new location to his list of delivery addresses.
    """
    def __init__(self):
        self.location = (0, 0)
        self.deliveries = [(0, 0), ]

    def move(self, direction):
        self.location = tuple([sum(coordinates) for coordinates
                               in zip(self.location, direction)])
        self.deliveries.append(self.location)

    def get_delivery_list(self):
        return self.deliveries


class DeliveryPlan(object):
    """
    Delivery Plan is the schedule Santas follow.
    It contains the number of Santas involved and gives them directions to go to.
    Delivery Plan can also count deliveries made by all Santas together.
    """
    def __init__(self, task_type):
        self.santa_count = TYPE[task_type]
        self.santas = [Santa() for count in xrange(self.santa_count)]

    def do_the_job(self, file_path):
        directions = parse_directions_file(file_path)
        return self.follow_directions(directions)

    def follow_directions(self, directions):
        turn = 0
        for direction in directions:
            turn = self.follow_direction(direction, turn)
        return self.count_deliveries()

    def follow_direction(self, direction, turn):
        self.santas[turn].move(parse_direction(direction))
        if turn == self.santa_count + TURN_SHIFT:
            return 0  # First Santa's turn (full circle)
        else:
            return turn + 1  # Next Santa's turn

    def count_deliveries(self):
        delivery_coverage = [delivery for santa in self.santas
                             for delivery in santa.get_delivery_list()]
        delivery_count = len(set(delivery_coverage))
        return delivery_count


def parse_directions_file(file_path):
    with open(file_path, 'r') as input_file:
        return input_file.read().strip("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_path')
    parser.add_argument('-t', action='store', dest='task_type', default='SILVER')
    args = parser.parse_args()
    delivery_plan = DeliveryPlan(args.task_type)
    print delivery_plan.do_the_job(args.file_path)


if __name__ == '__main__':
    main()
