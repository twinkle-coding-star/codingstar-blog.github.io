gradle 설정

dependencies

implementation 'com.android.support.recyclerview-(version)'

implementation 'com.android.support.cardview-(version)'



RecyclerView

리스트 항목을 구성하는 기존 뷰가 스크롤 되어 화면을 벗어났을 때, 새로운 뷰를 생성하지 않고 재사용한다.

성능적 유익이 있다.



3가지 레이아웃 매니저 사용 가능

LinearLayoutManager

GridLayoutManager

StaggeredGridLayoutManager



리스트 항목 생성

ViewHolder 클래스 사용



어뎁터

RecyclerView.Adapter



특이사항

AppBar, ToolBar와 사용시 스크롤 할 때 두 요소들을 사라지게 만들 수 있다.



CardView

런타임에 어떤 레이아웃 리소스라도 호출하여 표현 가능하다.



개발과정

CardView xml을 생성

- root layout을 CardView로 선택해야 한다.



 Recycler Adapter 생성

- RecyclerView.Adapter를 상속받되, 제너릭에는RecyclerView.ViewHolder를 상속받은 ViewHolder객체를 선언해줘야 한다.
- onCreateViewHolder
  - CardView xml을 inflate
  - ViewHolder 객체 인스턴스화(instantiate)
  - inflate로 얻은 View 객체를 ViewHolder에 넣어줌
- onBindViewHolder
  - ViewHolder 객체의 값, 표현되어야 할 값을 지정.
  - 두 번째 인자로 오는게 리스트 순서임

MainActivity

- RecyclerView 객체 생성
  - 레이아웃 매니저 지정
  - Adapter지정