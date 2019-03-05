데이터 모델 - 데이터 핸들러





Embedded RDBMS(Relational Database Management System)

Android, iOS 모두 사용

C언어로 개발

자바의 wrapper를 통해 SQLite에 접속



Cursor  Interface

데이터베이스 쿼리로 얻은 결과 세트에 읽기/쓰기의 임이 접근을 가능하도록 하는 인터페이스다.

Cursor의 구현은 동기화를 요구하지 않는다.

다중 쓰레드에서 커서를 사용할 경우에는, 자체적으로 동기화를 해주어야 한다.

AbstractCursor가 이 인터페이스를 구현한 대표적인 클래스이다.



SQLiteDatabase

Exposes methods to manage a SQLite database.

SQLiteDatabase has methods to create, delete, execute SQL commands, and perform other common database management tasks.

SQLiteOpenHelper

A helper class to manage database creation and version management.

You create a subclass implementing `onCreate(SQLiteDatabase)`, `onUpgrade(SQLiteDatabase, int, int)` and optionally `onOpen(SQLiteDatabase)`, and this class takes care of opening the database if it exists, creating it if it does not, and upgrading it as necessary. Transactions are used to make sure the database is always in a sensible state.

This class makes it easy for `ContentProvider` implementations to defer opening and upgrading the database until first use, to avoid blocking application startup with long-running database upgrades.

**Note:** this class assumes monotonically increasing version numbers for upgrades.



ContentValues

This class is used to store a set of values that the `ContentResolver` can process.