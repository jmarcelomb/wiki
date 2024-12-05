# Mockito Verify

## Verify simple invocation on mock 

```java
List<String> mockedList = mock(MyList.class);
mockedList.size();
verify(mockedList).size();
```

## Verify number of interactions with mock 

```java
List<String> mockedList = mock(MyList.class);
mockedList.size();
verify(mockedList, times(1)).size();
```

## Verify no interaction with the whole mock occurred 

```java
List<String> mockedList = mock(MyList.class);
verifyZeroInteractions(mockedList);
```

## Verify no interaction with a specific method occurred 

```java
List<String> mockedList = mock(MyList.class);
verify(mockedList, times(0)).size();
```

## Verify there are no unexpected interactions – this should fail: 

```java
List<String> mockedList = mock(MyList.class);
mockedList.size();
mockedList.clear();
verify(mockedList).size();
verifyNoMoreInteractions(mockedList);
```

## Verify order of interactions 

```java
List<String> mockedList = mock(MyList.class);
mockedList.size();
mockedList.add("a parameter");
mockedList.clear();

InOrder inOrder = Mockito.inOrder(mockedList);
inOrder.verify(mockedList).size();
inOrder.verify(mockedList).add("a parameter");
inOrder.verify(mockedList).clear();
```

## Verify an interaction has not occurred 

```java
List<String> mockedList = mock(MyList.class);
mockedList.size();
verify(mockedList, never()).clear();
```

## Verify an interaction has occurred at least certain number of times 

```java
List<String> mockedList = mock(MyList.class);
mockedList.clear();
mockedList.clear();
mockedList.clear();

verify(mockedList, atLeast(1)).clear();
verify(mockedList, atMost(10)).clear();
```

## Verify interaction with exact argument 

```java
List<String> mockedList = mock(MyList.class);
mockedList.add("test");
verify(mockedList).add("test");
```

## Verify interaction with flexible/any argument 

```java
List<String> mockedList = mock(MyList.class);
mockedList.add("test");
verify(mockedList).add(anyString());
```

## Verify interaction using argument capture 

```java
List<String> mockedList = mock(MyList.class);
mockedList.addAll(Lists.<String> newArrayList("someElement"));
ArgumentCaptor<List> argumentCaptor = ArgumentCaptor.forClass(List.class);
verify(mockedList).addAll(argumentCaptor.capture());
List<String> capturedArgument = argumentCaptor.<List<String>> getValue();
assertThat(capturedArgument, hasItem("someElement"));
```