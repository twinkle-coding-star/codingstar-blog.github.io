AppBar

상태바 (Status Bar)

툴바 (Tool Bar)

탭바 (Tab Bar)



스크롤이 생기는 영역

```xml
app:layout_behavior="@string/appbar_scrolling_view_behavior"
```



AppBarLayout 요소

```xml
app:layout_scrollFlags="scroll|enterAlways"
```



CollapsingToolbarLayout

AppBarLayout의 자식으로 설정



```xml
app:layout_collapseMode
```

- parallax : 앱 바가 사라질 때 콘텐트 뷰도 사라짐
- pin : 고정위치에 존재



```xml
app:layout_scrollFlags
```

- scroll|enterAlways
- scroll|enterAlways



```xml
app:contentScrim
```

- ?attr/색상







