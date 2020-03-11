### LRU

Least Recent Used

操作系统中的页面置换算法也有LRU，但是也可以推广到所有缓存替换算法，因为缓存的大小是有限的，所以当缓存满了的时候就要将按照一定的策略将东西换出去，这里
就是将最近最少访问的那一项移出去。

采用双端链表和字典来实现，双端链表插入时间是常数，删除中间某项时间是O(n)，但是如果通过字典记录下位置，那就可以在O(1)时间删除。

如果将一个东西放到缓存中，说明也是最近一次用的，所以是放到最前面，如果是更新某个值，也是一样，把这个值拿出来更新然后放到最前面（在实现中是将其先删除
然后再创建一个添加到首部）

主要支持两个操作，get和put，