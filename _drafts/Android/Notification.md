알림 생성

```java
NotificationCompat.Builder builder = new NotificationCompat.Builder(this).setSmallIcon(android.R.drawable.ic_dialog_info).setContentTitle("[제목]").setContentText("[내용]");
```



알림 전달

```java
NotificationManager notifyMgr =(NotificationManager)getSystemService(NOTIFICATION_SERVICE);
notifyMgr.notify([Notification ID : int], builder.build());
```



알림에서 액티비티로 인텐트 전달

```java
Intent toIntent = new Intent(this, NotifyDemoActivity.class);
PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, toIntent, PendingIntent.FLAG_UPDATE_CURRENT);
builder.setContentIntent(pendingIntent);
```

알림을 선택하면, toIntent에 속한 NotifyDemoActivity가 열린다



PendingIntent

인텐트를 다른 앱에 전달 할 수 있고, 전달 받은 앱이 향후에 그 인텐트를 수행할 수 있게 해준다.



알림에 Action 추가

```java
// 확인 안됨(Android 4.4 Kitkat)
NotificationCompat.Action action = new NotificationCompat.Action
                                                         .Builder(android.R.drawable.sym_action_chat,
                                                               "OPEN",
                                                                pendingIntent)
                                                         .build();
builder.addAction(action);
```

알림 밑에 OPEN 버튼이 생기고, pendingIntent가 전달하는 Activity로 돌아간다.





