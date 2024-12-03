---
title: shortlink copy
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# shortlink copy

Base URLs:

# Authentication

# 短链接后管监控

## GET 获取单个短链接监控

GET /stats

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|fullShortUrl|query|string| 否 |完整短链接|
|gid|query|string| 否 |分组标识|
|startDate|query|string| 否 |开始日期|
|endDate|query|string| 否 |结束日期|
|Authorization|header|string| 否 |token|

> 返回示例

```json
{
  "code": "0",
  "message": null,
  "data": {
    "pv": null,
    "uv": null,
    "uip": null,
    "daily": [
      {
        "date": "2023-11-14",
        "pv": 18,
        "uv": 2,
        "uip": 0
      },
      {
        "date": "2023-11-15",
        "pv": 2,
        "uv": 0,
        "uip": 0
      }
    ],
    "localeCnStats": [
      {
        "cnt": 4,
        "locale": "北京",
        "ratio": 0.17
      },
      {
        "cnt": 20,
        "locale": "未知",
        "ratio": 0.83
      }
    ],
    "hourStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      5,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      15
    ],
    "topIpStats": [
      {
        "cnt": 6,
        "ip": "127.0.0.2"
      },
      {
        "cnt": 2,
        "ip": "127.0.0.1"
      }
    ],
    "weekdayStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "browserStats": [
      {
        "cnt": 3,
        "browser": "Apple Safari",
        "ratio": 0.3
      },
      {
        "cnt": 4,
        "browser": "Google Chrome",
        "ratio": 0.4
      },
      {
        "cnt": 1,
        "browser": "Microsoft Edge",
        "ratio": 0.1
      },
      {
        "cnt": 2,
        "browser": "Google Chrome",
        "ratio": 0.2
      }
    ],
    "osStats": [
      {
        "cnt": 16,
        "os": "Mac OS",
        "ratio": 0.89
      },
      {
        "cnt": 2,
        "os": "Mac OS",
        "ratio": 0.11
      }
    ],
    "uvTypeStats": [
      {
        "cnt": 2,
        "uvType": "newUser",
        "ratio": 0.5
      },
      {
        "cnt": 2,
        "uvType": "oldUser",
        "ratio": 0.5
      }
    ],
    "deviceStats": [
      {
        "cnt": 3,
        "device": "Mobile",
        "ratio": 0.43
      },
      {
        "cnt": 4,
        "device": "PC",
        "ratio": 0.57
      }
    ],
    "networkStats": [
      {
        "cnt": 1,
        "network": "Mobile",
        "ratio": 0.5
      },
      {
        "cnt": 1,
        "network": "WIFI",
        "ratio": 0.5
      }
    ]
  },
  "requestId": null,
  "success": true
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|string|true|none||none|
|» message|null|true|none||none|
|» data|object|true|none||none|
|»» pv|null|true|none|PV|none|
|»» uv|null|true|none|UV|none|
|»» uip|null|true|none|UIP|none|
|»» daily|[object]|true|none|访问明细|none|
|»»» date|string|true|none|时间|none|
|»»» pv|integer|true|none|PV|none|
|»»» uv|integer|true|none|UV|none|
|»»» uip|integer|true|none|UIP|none|
|»» localeCnStats|[object]|true|none|访问地区|none|
|»»» cnt|integer|true|none|数量|none|
|»»» locale|string|true|none|地区名|none|
|»»» ratio|number|true|none|占比|none|
|»» hourStats|[integer]|true|none|24小时|none|
|»» topIpStats|[object]|true|none|高频访问IP|none|
|»»» cnt|integer|true|none||none|
|»»» ip|string|true|none||none|
|»» weekdayStats|[integer]|true|none|一周数据|none|
|»» browserStats|[object]|true|none|访问浏览器|none|
|»»» cnt|integer|true|none|数量|none|
|»»» browser|string|true|none|浏览器|none|
|»»» ratio|number|true|none|占比|none|
|»» osStats|[object]|true|none|访问操作系统|none|
|»»» cnt|integer|true|none|数量|none|
|»»» os|string|true|none|操作系统|none|
|»»» ratio|number|true|none|占比|none|
|»» uvTypeStats|[object]|true|none|访客类型|none|
|»»» cnt|integer|true|none|数量|none|
|»»» uvType|string|true|none|访客类型|newUser：新访客 oldUser：老访客|
|»»» ratio|number|true|none|占比|none|
|»» deviceStats|[object]|true|none|访问设备|none|
|»»» cnt|integer|true|none|数量|none|
|»»» device|string|true|none|访问设备|Mobile：移动设备 PC：电脑|
|»»» ratio|number|true|none|占比|none|
|»» networkStats|[object]|true|none|访问网络|none|
|»»» cnt|integer|true|none|数量|none|
|»»» network|string|true|none|访问网络|Mobile：移动数据 WIFI：WIFI|
|»»» ratio|number|true|none|占比|none|
|» requestId|null|true|none||none|
|» success|boolean|true|none||none|

## GET 获取分组短链接监控

GET /api/short-link/admin/v1/stats/group

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|gid|query|string| 否 |分组标识|
|startDate|query|string| 否 |开始日期|
|endDate|query|string| 否 |结束日期|
|Authorization|header|string| 否 |token|

> 返回示例

```json
{
  "code": "0",
  "message": null,
  "data": {
    "pv": null,
    "uv": null,
    "uip": null,
    "daily": [
      {
        "date": "2023-11-14",
        "pv": 18,
        "uv": 2,
        "uip": 0
      },
      {
        "date": "2023-11-15",
        "pv": 2,
        "uv": 0,
        "uip": 0
      }
    ],
    "localeCnStats": [
      {
        "cnt": 4,
        "locale": "北京",
        "ratio": 0.17
      },
      {
        "cnt": 20,
        "locale": "未知",
        "ratio": 0.83
      }
    ],
    "hourStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      5,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      15
    ],
    "topIpStats": [
      {
        "cnt": 6,
        "ip": "127.0.0.2"
      },
      {
        "cnt": 2,
        "ip": "127.0.0.1"
      }
    ],
    "weekdayStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "browserStats": [
      {
        "cnt": 3,
        "browser": "Apple Safari",
        "ratio": 0.3
      },
      {
        "cnt": 4,
        "browser": "Google Chrome",
        "ratio": 0.4
      },
      {
        "cnt": 1,
        "browser": "Microsoft Edge",
        "ratio": 0.1
      },
      {
        "cnt": 2,
        "browser": "Google Chrome",
        "ratio": 0.2
      }
    ],
    "osStats": [
      {
        "cnt": 16,
        "os": "Mac OS",
        "ratio": 0.89
      },
      {
        "cnt": 2,
        "os": "Mac OS",
        "ratio": 0.11
      }
    ],
    "uvTypeStats": [
      {
        "cnt": 2,
        "uvType": "newUser",
        "ratio": 0.5
      },
      {
        "cnt": 2,
        "uvType": "oldUser",
        "ratio": 0.5
      }
    ],
    "deviceStats": [
      {
        "cnt": 3,
        "device": "Mobile",
        "ratio": 0.43
      },
      {
        "cnt": 4,
        "device": "PC",
        "ratio": 0.57
      }
    ],
    "networkStats": [
      {
        "cnt": 1,
        "network": "Mobile",
        "ratio": 0.5
      },
      {
        "cnt": 1,
        "network": "WIFI",
        "ratio": 0.5
      }
    ]
  },
  "requestId": null,
  "success": true
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|string|true|none||none|
|» message|null|true|none||none|
|» data|object|true|none||none|
|»» pv|null|true|none|PV|none|
|»» uv|null|true|none|UV|none|
|»» uip|null|true|none|UIP|none|
|»» daily|[object]|true|none|访问明细|none|
|»»» date|string|true|none|时间|none|
|»»» pv|integer|true|none|PV|none|
|»»» uv|integer|true|none|UV|none|
|»»» uip|integer|true|none|UIP|none|
|»» localeCnStats|[object]|true|none|访问地区|none|
|»»» cnt|integer|true|none|数量|none|
|»»» locale|string|true|none|地区名|none|
|»»» ratio|number|true|none|占比|none|
|»» hourStats|[integer]|true|none|24小时|none|
|»» topIpStats|[object]|true|none|高频访问IP|none|
|»»» cnt|integer|true|none||none|
|»»» ip|string|true|none||none|
|»» weekdayStats|[integer]|true|none|一周数据|none|
|»» browserStats|[object]|true|none|访问浏览器|none|
|»»» cnt|integer|true|none|数量|none|
|»»» browser|string|true|none|浏览器|none|
|»»» ratio|number|true|none|占比|none|
|»» osStats|[object]|true|none|访问操作系统|none|
|»»» cnt|integer|true|none|数量|none|
|»»» os|string|true|none|操作系统|none|
|»»» ratio|number|true|none|占比|none|
|»» deviceStats|[object]|true|none|访问设备|none|
|»»» cnt|integer|true|none|数量|none|
|»»» device|string|true|none|访问设备|Mobile：移动设备 PC：电脑|
|»»» ratio|number|true|none|占比|none|
|»» networkStats|[object]|true|none|访问网络|none|
|»»» cnt|integer|true|none|数量|none|
|»»» network|string|true|none|访问网络|Mobile：移动数据 WIFI：WIFI|
|»»» ratio|number|true|none|占比|none|
|» requestId|null|true|none||none|
|» success|boolean|true|none||none|

## GET 获取单个短链接监控访问记录

GET /api/short-link/admin/v1/stats/access-record

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|fullShortUrl|query|string| 否 |完整短链接|
|gid|query|string| 否 |分组标识|
|startDate|query|string| 否 |开始日期|
|endDate|query|string| 否 |结束日期|
|current|query|integer| 否 |当前页|
|size|query|integer| 否 |每页大小|
|Authorization|header|string| 否 |token|

> 返回示例

```json
{
  "code": "0",
  "message": null,
  "data": {
    "pv": null,
    "uv": null,
    "uip": null,
    "daily": [
      {
        "date": "2023-11-14",
        "pv": 18,
        "uv": 2,
        "uip": 0
      },
      {
        "date": "2023-11-15",
        "pv": 2,
        "uv": 0,
        "uip": 0
      }
    ],
    "localeCnStats": [
      {
        "cnt": 4,
        "locale": "北京",
        "ratio": 0.17
      },
      {
        "cnt": 20,
        "locale": "未知",
        "ratio": 0.83
      }
    ],
    "hourStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      5,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      15
    ],
    "topIpStats": [
      {
        "cnt": 6,
        "ip": "127.0.0.2"
      },
      {
        "cnt": 2,
        "ip": "127.0.0.1"
      }
    ],
    "weekdayStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "browserStats": [
      {
        "cnt": 3,
        "browser": "Apple Safari",
        "ratio": 0.3
      },
      {
        "cnt": 4,
        "browser": "Google Chrome",
        "ratio": 0.4
      },
      {
        "cnt": 1,
        "browser": "Microsoft Edge",
        "ratio": 0.1
      },
      {
        "cnt": 2,
        "browser": "Google Chrome",
        "ratio": 0.2
      }
    ],
    "osStats": [
      {
        "cnt": 16,
        "os": "Mac OS",
        "ratio": 0.89
      },
      {
        "cnt": 2,
        "os": "Mac OS",
        "ratio": 0.11
      }
    ],
    "uvTypeStats": [
      {
        "cnt": 2,
        "uvType": "newUser",
        "ratio": 0.5
      },
      {
        "cnt": 2,
        "uvType": "oldUser",
        "ratio": 0.5
      }
    ],
    "deviceStats": [
      {
        "cnt": 3,
        "device": "Mobile",
        "ratio": 0.43
      },
      {
        "cnt": 4,
        "device": "PC",
        "ratio": 0.57
      }
    ],
    "networkStats": [
      {
        "cnt": 1,
        "network": "Mobile",
        "ratio": 0.5
      },
      {
        "cnt": 1,
        "network": "WIFI",
        "ratio": 0.5
      }
    ]
  },
  "requestId": null,
  "success": true
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|string|true|none||none|
|» message|null|true|none||none|
|» data|object|true|none||none|
|»» size|integer|true|none||none|
|»» current|integer|true|none||none|
|»» records|[object]|true|none||none|
|»»» uvType|string|true|none|访客类型|none|
|»»» browser|string|true|none|浏览器|none|
|»»» os|string|true|none|操作系统|none|
|»»» ip|string|true|none|IP|none|
|»»» network|string¦null|true|none|访问网络|none|
|»»» device|string¦null|true|none|访问设备|none|
|»»» locale|string¦null|true|none|访问地区|none|
|»»» createTime|string|true|none|访问时间|none|
|»» pages|integer|true|none||none|
|»» total|integer|true|none||none|
|» requestId|null|true|none||none|
|» success|boolean|true|none||none|

## GET 获取分组短链接监控访问记录

GET /api/short-link/admin/v1/stats/access-record/group

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|gid|query|string| 否 |分组标识|
|startDate|query|string| 否 |开始日期|
|endDate|query|string| 否 |结束日期|
|current|query|integer| 否 |当前页|
|size|query|integer| 否 |每页大小|
|Authorization|header|string| 否 |token|

> 返回示例

```json
{
  "code": "0",
  "message": null,
  "data": {
    "pv": null,
    "uv": null,
    "uip": null,
    "daily": [
      {
        "date": "2023-11-14",
        "pv": 18,
        "uv": 2,
        "uip": 0
      },
      {
        "date": "2023-11-15",
        "pv": 2,
        "uv": 0,
        "uip": 0
      }
    ],
    "localeCnStats": [
      {
        "cnt": 4,
        "locale": "北京",
        "ratio": 0.17
      },
      {
        "cnt": 20,
        "locale": "未知",
        "ratio": 0.83
      }
    ],
    "hourStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      5,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      15
    ],
    "topIpStats": [
      {
        "cnt": 6,
        "ip": "127.0.0.2"
      },
      {
        "cnt": 2,
        "ip": "127.0.0.1"
      }
    ],
    "weekdayStats": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "browserStats": [
      {
        "cnt": 3,
        "browser": "Apple Safari",
        "ratio": 0.3
      },
      {
        "cnt": 4,
        "browser": "Google Chrome",
        "ratio": 0.4
      },
      {
        "cnt": 1,
        "browser": "Microsoft Edge",
        "ratio": 0.1
      },
      {
        "cnt": 2,
        "browser": "Google Chrome",
        "ratio": 0.2
      }
    ],
    "osStats": [
      {
        "cnt": 16,
        "os": "Mac OS",
        "ratio": 0.89
      },
      {
        "cnt": 2,
        "os": "Mac OS",
        "ratio": 0.11
      }
    ],
    "uvTypeStats": [
      {
        "cnt": 2,
        "uvType": "newUser",
        "ratio": 0.5
      },
      {
        "cnt": 2,
        "uvType": "oldUser",
        "ratio": 0.5
      }
    ],
    "deviceStats": [
      {
        "cnt": 3,
        "device": "Mobile",
        "ratio": 0.43
      },
      {
        "cnt": 4,
        "device": "PC",
        "ratio": 0.57
      }
    ],
    "networkStats": [
      {
        "cnt": 1,
        "network": "Mobile",
        "ratio": 0.5
      },
      {
        "cnt": 1,
        "network": "WIFI",
        "ratio": 0.5
      }
    ]
  },
  "requestId": null,
  "success": true
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|string|true|none||none|
|» message|null|true|none||none|
|» data|object|true|none||none|
|»» size|integer|true|none||none|
|»» current|integer|true|none||none|
|»» records|[object]|true|none||none|
|»»» uvType|string|true|none|访客类型|none|
|»»» browser|string|true|none|浏览器|none|
|»»» os|string|true|none|操作系统|none|
|»»» ip|string|true|none|IP|none|
|»»» network|string¦null|true|none|访问网络|none|
|»»» device|string¦null|true|none|访问设备|none|
|»»» locale|string¦null|true|none|访问地区|none|
|»»» createTime|string|true|none|访问时间|none|
|»» pages|integer|true|none||none|
|»» total|integer|true|none||none|
|» requestId|null|true|none||none|
|» success|boolean|true|none||none|

# 数据模型

