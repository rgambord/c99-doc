.. _9899_B.22:

B.22 Date and time \<time.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    NULL                  size_t                  time_t
    CLOCKS_PER_SEC        clock_t                 struct tm

    clock_t clock(void);
    double difftime(time_t time1, time_t time0);
    time_t mktime(struct tm *timeptr);
    time_t time(time_t *timer);
    char *asctime(const struct tm *timeptr);
    char *ctime(const time_t *timer);
    struct tm *gmtime(const time_t *timer);
    struct tm *localtime(const time_t *timer);
    size_t strftime(char *restrict s, size_t maxsize, const char *restrict format,
                    const struct tm *restrict timeptr);

