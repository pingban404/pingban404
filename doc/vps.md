# 指南 - VPS - SSV

## 两大类

*第一种（自建）*

 - [八合一脚本](https://github.com/mack-a/v2ray-agent?tab=readme-ov-file)
 - [X-UI面板](https://bulianglin.com/archives/nicename.html) 

*第二种（使用机场）*
 - 使用别人的服务器
   - https://clashx.pro/airport-recommendation
   - https://github.com/hwanz/SSR-V2ray-Trojan

## 基础概念

*自建服务器*
 - VPS购买
 - 域名购买（可选）
 - 服务端软件
 - 客户端软件
  
*使用机场*
 - 客户端软件
 - 机场服务商选择

## 网络中客户端安装位置

*个人使用*
 - 安装客户端(分流)


*多人使用*
 - 需要一台路由器(分流)
  
## 需要注意事项

*自建服务器* 

- 策略控制（防止国内流量回流）
- 协议选择 (国内有时会对某些协议特殊关照)
- 推荐协议（组合使用）
  - VMess (国内->国外)
  - [VLESS](https://github.com/v2fly/v2ray-core/)
  - TROJAN (国内->国外)
  - SHADOWSOCKS(国内->国内->其他协议->国外)避免回流  （机场供应商常用）
  - TCP +其他协议组合
  - [vision] (https://github.com/v2fly/)