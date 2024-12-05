"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

import os
from typing import Any, Callable, List, Optional, cast

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg, tool
from typing_extensions import Annotated

from src.react_agent.configuration import Configuration

import requests

BASE_URL = os.environ.get("BASE_URL")


@tool
async def search(
    query: str, *, config: Annotated[RunnableConfig, InjectedToolArg]
) -> Optional[list[dict[str, Any]]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    configuration = Configuration.from_runnable_config(config)
    wrapped = TavilySearchResults(max_results=configuration.max_search_results)
    result = await wrapped.ainvoke({"query": query})
    return cast(list[dict[str, Any]], result)




@tool
async def get_short_link_status(
    fullShortUrl: Optional[str] = None,
    gid: Optional[str] = None,
    startDate: Optional[str] = None,
    endDate: Optional[str] = None,
    Authorization: Optional[str] = None,
):
    """
    Get short URL status from a backend API.

    Args:
        fullShortUrl: The full short URL.
        gid: The group ID.
        startDate: The start date.
        endDate: The end date.
        Authorization: The authorization token.

    Returns:
        a dict of short link status.

    """


    url = f"{BASE_URL}/stats"

    body = {
        "fullShortUrl": fullShortUrl,
        "gid": gid,
        "startDate": startDate,
        "endDate": endDate,
    }


    headers = {
        "Authorization": Authorization,
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

    try:
        response = requests.get(url, params=body, headers=headers)
        print(response.json())
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    return response.json()


@tool
async def get_short_link_group(
    gid: Optional[str] = None,
    startDate: Optional[str] = None,
    endDate: Optional[str] = None,
    Authorization: Optional[str] = None,
):
    """
    Get short URL group from a backend API.

    Args:
        gid: The group ID.
        startDate: The start date.
        endDate: The end date.
        Authorization: The authorization token.

    Returns:
        a dict of short link group status.

    """


    url = f"{BASE_URL}/api/short-link/admin/v1/stats/group"

    body = {
        "gid": gid,
        "startDate": startDate,
        "endDate": endDate,
    }

    headers = {
        "Authorization": Authorization,
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

    try:
        response = requests.get(url, params=body, headers=headers)
        print(response.json())
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    return response.json()



@tool
async def get_one_short_link_access_record(
    fullShortUrl: Optional[str] = None,
    gid: Optional[str] = None,
    startDate: Optional[str] = None,
    endDate: Optional[str] = None,
    current: Optional[int] = None,
    size: Optional[int] = None,
    Authorization: Optional[str] = None,
):
    """
    Get short URL access record from a backend API.

    Args:
        fullShortUrl: The full short URL.
        gid: The group ID.
        startDate: The start date.
        endDate: The end date.
        current: The current page.
        size: The page size.
        Authorization: The authorization token.

    Returns:
        a dict of short link access record.
    """

    url = f"{BASE_URL}/api/short-link/admin/v1/stats/access-record"

    body = {
            "fullShortUrl": fullShortUrl,
            "gid": gid,
            "startDate": startDate,
            "endDate": endDate,
            "current": current,
            "size": size,
        }

    headers = {
        "Authorization": Authorization,
        "Accept": "*/*",
        "Connection": "keep-alive",
        }

    try:
        response = requests.get(url, params=body, headers=headers)
        print(response.json())
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    return response.json()

# gid	query	string	否	分组标识
# startDate	query	string	否	开始日期
# endDate	query	string	否	结束日期
# current	query	integer	否	当前页
# size	query	integer	否	每页大小
# Authorization	header	string	否	token
@tool
async def get_short_link_group_access_record(
    gid: Optional[str] = None,
    startDate: Optional[str] = None,
    endDate: Optional[str] = None,
    current: Optional[int] = None,
    size: Optional[int] = None,
    Authorization: Optional[str] = None,
):
    """
    Get short URL group access record from a backend API.

    Args:
        gid: The group ID.
        startDate: The start date.
        endDate: The end date.
        current: The current page.
        size: The page size.
        Authorization: The authorization token.

    Returns:
        a dict of short link group access record.
    """

    url = f"{BASE_URL}/api/short-link/admin/v1/stats/access-record/group"

    body = {
            "gid": gid,
            "startDate": startDate,
            "endDate": endDate,
            "current": current,
            "size": size,
        }

    headers = {
        "Authorization": Authorization,
        "Accept": "*/*",
        "Connection": "keep-alive",
        }

    try:
        response = requests.get(url, params=body, headers=headers)
        print(response.json())
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    return response.json()



MONITOR_TOOLS= [
    get_short_link_status,
    get_short_link_group,
    get_one_short_link_access_record,
    get_short_link_group_access_record
    ]

# {
#     "domain": "http://www.baidu.com",
#     "originUrl": "https://www.yuque.com/xiangxinliao-bb1ly",
#     "gid": "0",
#     "createdType": 1,
#     "validDateType": 1,
#     "validDate": "",
#     "describe": "yuque-miirso"
# }
@tool
async def create_short_link(
    domain: Optional[str] = None,
    originUrl: Optional[str] = None,
    gid: Optional[str] = None,
    createdType: Optional[int] = None,
    validDateType: Optional[int] = None,
    validDate: Optional[str] = None,
    describe: Optional[str] = None,
):
    """
    Create short URL

    Args:
        domain: The domain.
        originUrl: The original URL.
        gid: The group ID.
        createdType: The created type.
        validDateType: The valid date type.
        validDate: The valid date.
        describe: The description.

    Returns:
        a dict of short link.
    """

    url = f"{BASE_URL}/create"

    body = {
        "domain": domain,
        "originUrl": originUrl,
        "gid": gid,
        "createdType": createdType,
        "validDateType": validDateType,
        "validDate": validDate,
        "describe": describe,
    }

    headers = {
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

    try:
        response = requests.post(url, params=body, headers=headers)
        print(response.json())
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    return response.json()

MANAGER_TOOLS = [
    create_short_link
]


SUPPORT_TOOLS = [
    search
]
