#include <stdio.h>
#include <stdint.h>
#include <time.h>

int main() {
  int l1[] = {1,2,3};
  int l2[] = {4,5,6};
  int l3[] = {7};
  int l4[] = {8,9};
  int* l[4*99];
  for (int i = 0; i < 99; i++) {
    l[i*4] = l1;
    l[i*4+1] = l2;
    l[i*4+2] = l3;
    l[i*4+3] = l4;
  }
  int lout[9*99];

  struct timespec stop, start;
  clock_gettime(CLOCK_MONOTONIC_RAW, &start);

  int max_loop = 10000000;
  for (int loop = 0; loop < max_loop; loop++) {
    for (int i = 0; i < 99; i++) {
      lout[i*9] = l[i*4][0]+loop;
      lout[i*9+1] = l[i*4][1]+loop;
      lout[i*9+2] = l[i*4][2]+loop;
      lout[i*9+3] = l[i*4+1][0]+loop;
      lout[i*9+4] = l[i*4+1][1]+loop;
      lout[i*9+5] = l[i*4+1][2]+loop;
      lout[i*9+6] = l[i*4+2][0]+loop;
      lout[i*9+7] = l[i*4+3][0]+loop;
      lout[i*9+8] = l[i*4+3][1]+loop;
    }
  }

  clock_gettime(CLOCK_MONOTONIC_RAW, &stop);

  for (int i = 0; i < 9*99; i++) {
    printf("%d ", lout[i]);
  }

  uint64_t delta_us = (stop.tv_sec - start.tv_sec) * 1000000 + (stop.tv_nsec - start.tv_nsec) / 1000;
  printf("\n\ntime in ns %llu\n", delta_us*1000/max_loop);
  return 0;
}
