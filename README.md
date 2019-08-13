BoomFish
===================

## Need
`flask`  `sqlite`  `docker`  `nginx`  `uwsgi`  `redis`

## Build and Run
```
    // docker bulid -t boomfish .
    docker bulid -t boomfish https://github.com/Hcreak/boomfish.git
    docker run -d -p 5000:80 --name BOOM boomfish

```

##  Notes

> * 调用gravatar的ssl链接 速度能快点
> * 解决时区问题（CTS） 修改dockerfile 
> * 调整dockerfile构建顺序
> * ~~Redis作为索引列表缓存~~
> * 全部采用Redis 关闭持久化仅作为缓存使用
> * 精简css
