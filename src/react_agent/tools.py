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


# |名称|位置|类型|必选|说明|
# |---|---|---|---|---|
# |fullShortUrl|query|string| 否 |完整短链接|
# |gid|query|string| 否 |分组标识|
# |startDate|query|string| 否 |开始日期|
# |endDate|query|string| 否 |结束日期|
# |Authorization|header|string| 否 |token|
# |名称|类型|必选|约束|中文名|说明|
# |---|---|---|---|---|---|
# |» code|string|true|none||none|
# |» message|null|true|none||none|
# |» data|object|true|none||none|
# |»» pv|null|true|none|PV|none|
# |»» uv|null|true|none|UV|none|
# |»» uip|null|true|none|UIP|none|
# |»» daily|[object]|true|none|访问明细|none|
# |»»» date|string|true|none|时间|none|
# |»»» pv|integer|true|none|PV|none|
# |»»» uv|integer|true|none|UV|none|
# |»»» uip|integer|true|none|UIP|none|
# |»» localeCnStats|[object]|true|none|访问地区|none|
# |»»» cnt|integer|true|none|数量|none|
# |»»» locale|string|true|none|地区名|none|
# |»»» ratio|number|true|none|占比|none|
# |»» hourStats|[integer]|true|none|24小时|none|
# |»» topIpStats|[object]|true|none|高频访问IP|none|
# |»»» cnt|integer|true|none||none|
# |»»» ip|string|true|none||none|
# |»» weekdayStats|[integer]|true|none|一周数据|none|
# |»» browserStats|[object]|true|none|访问浏览器|none|
# |»»» cnt|integer|true|none|数量|none|
# |»»» browser|string|true|none|浏览器|none|
# |»»» ratio|number|true|none|占比|none|
# |»» osStats|[object]|true|none|访问操作系统|none|
# |»»» cnt|integer|true|none|数量|none|
# |»»» os|string|true|none|操作系统|none|
# |»»» ratio|number|true|none|占比|none|
# |»» uvTypeStats|[object]|true|none|访客类型|none|
# |»»» cnt|integer|true|none|数量|none|
# |»»» uvType|string|true|none|访客类型|newUser：新访客 oldUser：老访客|
# |»»» ratio|number|true|none|占比|none|
# |»» deviceStats|[object]|true|none|访问设备|none|
# |»»» cnt|integer|true|none|数量|none|
# |»»» device|string|true|none|访问设备|Mobile：移动设备 PC：电脑|
# |»»» ratio|number|true|none|占比|none|
# |»» networkStats|[object]|true|none|访问网络|none|
# |»»» cnt|integer|true|none|数量|none|
# |»»» network|string|true|none|访问网络|Mobile：移动数据 WIFI：WIFI|
# |»»» ratio|number|true|none|占比|none|
# |» requestId|null|true|none||none|
# |» success|boolean|true|none||none|

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
    # Returns:
    #     pv: The page views.
    #     uv: The unique visitors.
    #     uip: The unique IP addresses.
    #     daily: The daily visit details.
    #     localeCnStats: The visit locations.
    #     hourStats: The hourly visit details.
    #     topIpStats: The top IP addresses.
    #     weekdayStats: The weekly visit details.
    #     browserStats: The browser statistics.
    #     osStats: The operating system statistics.
    #     uvTypeStats: The visitor type statistics.
    #     deviceStats: The device statistics.
    #     networkStats: The network statistics.
    # """

    url = f"{BASE_URL}/stats"

    body = {
        "fullShortUrl": fullShortUrl,
        "gid": gid,
        "startDate": startDate,
        "endDate": endDate,
    }

# --header 'Accept: */*' \
#          --header 'Host: 127.0.0.1:4523' \
#                   --header 'Connection: keep-alive'
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

# |gid|query|string| 否 |分组标识|
# |startDate|query|string| 否 |开始日期|
# |endDate|query|string| 否 |结束日期|
# |Authorization|header|string| 否 |token|
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
    # Returns:
    #     pv: The page views.
    #     uv: The unique visitors.
    #     uip: The unique IP addresses.
    #     daily: The daily visit details.
    #     localeCnStats: The visit locations.
    #     hourStats: The hourly visit details.
    #     topIpStats: The top IP addresses.
    #     weekdayStats: The weekly visit details.
    #     browserStats: The browser statistics.
    #     osStats: The operating system statistics.
    #     uvTypeStats: The visitor type statistics.
    #     deviceStats: The device statistics.
    #     networkStats: The network statistics.
    # """

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


# fullShortUrl	query	string	否	完整短链接
# gid	query	string	否	分组标识
# startDate	query	string	否	开始日期
# endDate	query	string	否	结束日期
# current	query	integer	否	当前页
# size	query	integer	否	每页大小
# Authorization	header	string	否	token
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
