#problem:->  https://bit.ly/2ZFymNn

#include<stdio.h>
void main()  
{
	long long int n;
 	int m,i,j,k,sum,max;
	scanf("%lld",&n);
	long long int a[n];
	int sums[n];
	for(i=0;i<n;i++)
	{
		scanf("%lld",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		sum=0;
		j=1;
		m=i;
		while(m+j<=n)
		{
			for(k=m;k<m+j;k++)
			{
				sum = sum + a[k];
			}
			m=m+j;
			j=j+1;
		}
		sums[i]=sum;
	}
	max = sums[0];
	for(i=1;i<n;i++)
	{
		if(max<sums[i])
		{
			max = sums[i];
		}
	}
	printf("%d",max);
}
