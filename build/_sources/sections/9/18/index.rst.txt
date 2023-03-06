.. _9899_B.18:

B.18 Input/output \<stdio.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    size_t          _IOLBF            FILENAME_MAX      TMP_MAX
    FILE            _IONBF            L_tmpnam          stderr
    fpos_t          BUFSIZ            SEEK_CUR          stdin
    NULL            EOF               SEEK_END          stdout
    _IOFBF          FOPEN_MAX         SEEK_SET

    int remove(const char *filename);
    int rename(const char *old, const char *new);
    FILE *tmpfile(void);
    char *tmpnam(char *s);
    int fclose(FILE *stream);
    int fflush(FILE *stream);
    FILE *fopen(const char *restrict filename, const char *restrict mode);
    FILE *freopen(const char *restrict filename, const char *restrict mode,
                  FILE *restrict stream);
    void setbuf(FILE *restrict stream, char *restrict buf);
    int setvbuf(FILE *restrict stream, char *restrict buf, int mode, size_t size);
    int fprintf(FILE *restrict stream, const char *restrict format, ...);
    int fscanf(FILE *restrict stream, const char *restrict format, ...);
    int printf(const char *restrict format, ...);
    int scanf(const char *restrict format, ...);
    int snprintf(char *restrict s, size_t n, const char *restrict format, ...);
    int sprintf(char *restrict s, const char *restrict format, ...);
    int sscanf(const char *restrict s, const char *restrict format, ...);
    int vfprintf(FILE *restrict stream, const char *restrict format, va_list arg);
    int vfscanf(FILE *restrict stream, const char *restrict format, va_list arg);
    int vprintf(const char *restrict format, va_list arg);
    int vscanf(const char *restrict format, va_list arg);
    int vsnprintf(char *restrict s, size_t n, const char *restrict format,
                  va_list arg);
    int vsprintf(char *restrict s, const char *restrict format, va_list arg);
    int vsscanf(const char *restrict s, const char *restrict format, va_list arg);
    int fgetc(FILE *stream);
    char *fgets(char *restrict s, int n, FILE *restrict stream);
    int fputc(int c, FILE *stream);
    int fputs(const char *restrict s, FILE *restrict stream);
    int getc(FILE *stream);
    int getchar(void);
    char *gets(char *s);
    int putc(int c, FILE *stream);
    int putchar(int c);
    int puts(const char *s);
    int ungetc(int c, FILE *stream);
    size_t fread(void *restrict ptr, size_t size, size_t nmemb,
                FILE *restrict stream);
    size_t fwrite(const void *restrict ptr, size_t size, size_t nmemb,
                  FILE *restrict stream);
    int fgetpos(FILE *restrict stream, fpos_t *restrict pos);
    int fseek(FILE *stream, long int offset, int whence);
    int fsetpos(FILE *stream, const fpos_t *pos);
    long int ftell(FILE *stream);
    void rewind(FILE *stream);
    void clearerr(FILE *stream);
    int feof(FILE *stream);
    int ferror(FILE *stream);
    void perror(const char *s);

