## 小工具集合

* resize.py

  >    修改安卓图片资源文件大小，根据`mipmap-xxhdpi`图片生成其他格式的图片

  ```shell
  python3 resize.py android
  # android的为文件名，文件里面包含一个名为mipmap-xxhdpi的文件，
  # 运行命令后将会生成`mipmap-hdpi` `mipmap-mhdpi` `mipmap-xhdpi` 文件的资源文件
  ```

* iosResize.py

  > 生成iOS的图片文件工具

  ```shell
  python3 iosResize.py icon.png
  # icon.png 原始的图片 3x
  # 运行之后会生成 1x， 2x， 3x的图片资源放在iso文件夹下
  ```

* convertPng2Jpg.py

  > 将png图片转换成jpg

  ```shell
  python3 convertPng2Jpg.py 背面.png 
  ```

* png2webp.py

  > 将png图片转换成webp[需要 [cwebp](https://developers.google.com/speed/webp/docs/cwebp) 首先安装webp ```sudo apt install webp``` ]

  ```shell
  python3 png2webp.py -i img/
  ```
  
* translang/

  > 将安卓文字资源文件存储到sqlite数据库

  ```shell
  python3 tocXml2db.py . 
  ```

  > 将数据库的多语言转换成excel文件

  ```shell
  python3 exel.py language.db
  ```

  