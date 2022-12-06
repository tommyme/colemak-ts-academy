# colemak-academy ts version
[源站 代码都是开源的](https://www.colemak.academy/)

想改一下单词的生成逻辑，让我们可以自行练习

主要是我数字打的不好，另外我打大写还是用的魔法（长按space变成shift），想改回来，所以需要一些自定义的生成策略
## 网页版
修改工作还在继续，暂时的成果就是成功迁移到了ts上面，能跑

不过仍然有很多的语法错误，代码太多了，手工改太麻烦，之后可能改 可能不改

原版就是放了一个mask 其实可以自己写个vue版本的
```css
-webkit-mask-image: -webkit-gradient(linear, left top, right bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)));
```

- how to build

```shell
pnpm i -g typescript
tsc
```

## 终端版本

```shell
python3 main2.py
```

