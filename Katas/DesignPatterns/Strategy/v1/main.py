from participant import Participant
from event import Event
from marathon_competitor_strategy import MarathonCompetitorStrategy
from maraton_strategy import MarathonStrategy


def main():
    competitors = [
        Participant(
            name='Alice',
            action_strategy=MarathonCompetitorStrategy()
        ),
        Participant(
            name='Bob',
            action_strategy=MarathonCompetitorStrategy()
        ),
        Participant(
            name='Charlie',
            action_strategy=MarathonCompetitorStrategy()
        ),
    ]
    event = Event(
        name='Marathon XYZ',
        event_strategy=MarathonStrategy(
            distance=60
        ),
        participants=competitors,
        max_ticks=1000
    )
    event.run()


if __name__ == "__main__":
    main()