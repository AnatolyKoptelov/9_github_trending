import requests
import argparse
from datetime import datetime, timedelta


def get_args():
    parser = argparse.ArgumentParser(
        description='GitHub Trending'
    )
    parser.add_argument(
        '-q',
        '--quantity',
        type=int,
        default=20,
        help='{}{}'.format(
            'How much repositories to display',
            'Using 20 by default',
        )
    )
    parser.add_argument(
        '-d',
        '--days',
        type=int,
        default=7,
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


def get_open_issues_amount(repo_owner, repo_name):
    url = '{}{}/{}/{}'.format(
        'https://api.github.com/repos/',
        repo_owner,
        repo_name,
        'issues',
    )
    response = requests.get(url)
    if response.ok:
        return len(response.json())


def format_for_print(repository_data, amount):
    length_of_date_string = 10
    return '{:70}\t{:12}\t{:5}\t{:13}'.format(
        repository_data['html_url'],
        repository_data['created_at'][:length_of_date_string],
        repository_data['stargazers_count'],
        amount,
    )


if __name__ == '__main__':
    trending_repositories = None
    open_issues_amount = []
    args = get_args()
    try:
        trending_repositories = get_trending_repositories(
            args.quantity,
            datetime.strftime(
                datetime.now() - timedelta(days=args.days),
                '%Y-%m-%d',
            )
        )
        open_issues_amount = trending_repositories and [
            get_open_issues_amount(
                repository['owner']['login'],
                repository['name'],
            ) for repository in trending_repositories
        ] or None
    except requests.exceptions.RequestException as error:
        print(error)
    if trending_repositories and open_issues_amount:
        print('{:70}\t{:12}\t{:5}\t{:13}'.format(
            'HTML URL of the Trending Repository',
            'Was created',
            'Stars',
            'Opened issues',
        ))
        for position, repository in enumerate(trending_repositories):
            print(format_for_print(repository, open_issues_amount[position]))
    else:
        print('Cannot read repositories data. Try again later!')
