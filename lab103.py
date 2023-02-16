import httpx
from prefect import flow, task
from prefect.blocks.system import Secret
from prefect.tasks import task_input_hash

secret_block = Secret.load("alpha-vantage")

# Access the stored secret
secret_block.get()


@task(cache_key_fn=task_input_hash)
def get_data(symbol="IBM", interval="5min"):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={secret_block}"
    response = httpx.get(url)
    data = response.json()
    return data


@flow
def get_metadata(data):
    return data["Meta Data"]


@flow
def main(symbol="IBM", interval="5min"):
    data = get_data()
    md = get_metadata(data)
    print(md)


if __name__ == "__main__":
    main()
