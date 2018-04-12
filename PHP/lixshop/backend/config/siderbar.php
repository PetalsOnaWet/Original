<?php

return [
    [
        'realData' => true,
        'title' => '首页',
        'icon' => 'fa-tachometer',
        'redirect' => '../home/index',
        'data' => [],
    ],
    [
        'realData' => false,
        'title' => '产品管理',
        'icon' => 'fa-desktop',
        'redirect' => '../product/index',
        'data' => [
            [
                'title' => '产品信息管理',
                'redirect' => '../product/index',
            ],
            [   
                'title' => '产品评论管理', 
                'redirect' => '/home/index',
            ],
            [
                'title' => '产品收藏管理',
                'redirect' => '/home/index',
            ],
        ],
    ],
    [
        'realData' => false,
        'title' => '销售',
        'icon' => 'fa-cc-visa',
        'redirect' => '/home/index',
        'data' => [
            [
                'title' => '订单管理',
                'redirect' => '/home/index',
            ],
            [
                'title' => '优惠券',
                'redirect' => '/home/index',
            ]
        ],
    ],
    [
        'realData' => false,
        'title' => '用户管理',
        'icon' => 'fa-user-plus',
        'redirect' => '/home/index',
        'data' => [
            [
                'title' => '账号管理',
                'redirect' => '/home/index',
            ],
        ],
    ],
    [
        'realData' => false,
        'title' => '控制面板',
        'icon' => 'fa-paperclip',
        'redirect' => '/home/index',
        'data' => [
            [
                'title' => '我的账户',
                'redirect' => '/home/index',
            ],
            [
                'title' => '账户管理',
                'redirect' => '/home/index',
            ],
            [
                'title' => '权限管理',
                'redirect' => '/home/index',
            ],
            [
                'title' => '操作日志',
                'redirect' => '/home/index',
            ],
        ],
    ]
];
