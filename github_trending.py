import requests
import argparse
from datetime import datetime, timedelta


def get_args():
    default_quantity = 20
    default_period = 7
    parser = argparse.ArgumentParser(
        description='GitHub Trending'
    )
    parser.add_argument(
        '-q',
        '--quantity',
        type=int,
        default=default_quantity,
        help='{}{}'.format(
            'How much repositories to display',
            'Using 20 by default',
        )
    )
    parser.add_argument(
        '-d',
        '--days',
        type=int,
        default=default_period,
        help='{}{}'.format(
            'How long ago repositories were created',
            'Using 7 days by default',
        )
    )
    return parser.parse_args()


def get_trending_repositories(top_size, created_after):
    url = 'https://api.github.com/search/repositories'
    get_params = {
        'q': '{}{}'.format(
            'created:>=',
            created_after,
        ),
        'sort': 'stars'
    }
    response = requests.get(url, params=get_params)
    if response.ok:
        return response.json()['items'][:top_size]


def repository_for_print(repository_data):
    length_of_date_string = len('YYYY-MM-DD')
    return '{:60}\t{:12}\t{:5}\t{:13}'.format(
        repository_data['html_url'],
        repository_data['created_at'][:length_of_date_string],
        repository_data['stargazers_count'],
        repository_data['open_issues_count'],
    )


if __name__ == '__main__':
    args = get_args()
    try:
        trending_repositories = get_trending_repositories(
            args.quantity,
            datetime.strftime(
                datetime.now() - timedelta(days=args.days),
                '%Y-%m-%d',
            )
        )
        print('{:60}\t{:12}\t{:5}\t{:13}'.format(
            'HTML URL of the Trending Repository',
            'Was created',
            'Stars',
            'Opened issues',
        ))
        for repository in trending_repositories:
            print(repository_for_print(repository))
    except requests.exceptions.RequestException as error:
        print(error)