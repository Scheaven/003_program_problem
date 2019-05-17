#include <stdio.h>
#include <stdlib.h>
/*
	https://www.nowcoder.com/practice/3fbd8fe929ea4eb3a254c0ed34ac993a?tpId=90&tqId=30782&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking
	算法思想：从头向尾遍历，记录最长的字符串记录；
*/

int main()
{
	char line[50]; //定义两个字符数组
	int maxlen = 1;
	int currlen = 1;
	scanf("%s", line);
	char curr = line[0];
	for(int i = 1;i<strlen(line);i++)
	{
		printf("%c,,%c,,,%d\n",curr,line[i],curr != line[i] );
		if (curr != line[i])
		{
			curr = line[i];
			currlen++;
		}else{
			currlen = 1;
		}
			maxlen = currlen>maxlen?currlen:maxlen;
	}
	printf("%d\n", maxlen);
	system("pause");
	return 0;
}
