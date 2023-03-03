.. _9899_B.7:

B.7 Format conversion of integer types \<inttypes.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    imaxdiv_t
    PRIdN        PRIdLEASTN        PRIdFASTN        PRIdMAX     PRIdPTR
    PRIiN        PRIiLEASTN        PRIiFASTN        PRIiMAX     PRIiPTR
    PRIoN        PRIoLEASTN        PRIoFASTN        PRIoMAX     PRIoPTR
    PRIuN        PRIuLEASTN        PRIuFASTN        PRIuMAX     PRIuPTR
    PRIxN        PRIxLEASTN        PRIxFASTN        PRIxMAX     PRIxPTR
    PRIXN        PRIXLEASTN        PRIXFASTN        PRIXMAX     PRIXPTR
    SCNdN        SCNdLEASTN        SCNdFASTN        SCNdMAX     SCNdPTR
    SCNiN        SCNiLEASTN        SCNiFASTN        SCNiMAX     SCNiPTR
    SCNoN        SCNoLEASTN        SCNoFASTN        SCNoMAX     SCNoPTR
    SCNuN        SCNuLEASTN        SCNuFASTN        SCNuMAX     SCNuPTR
    SCNxN        SCNxLEASTN        SCNxFASTN        SCNxMAX     SCNxPTR

    intmax_t imaxabs(intmax_t j);
    imaxdiv_t imaxdiv(intmax_t numer, intmax_t denom);
    intmax_t strtoimax(const char *restrict nptr, char **restrict endptr, int base);
    uintmax_t strtoumax(const char *restrict nptr, char **restrict endptr,
                        int base);
    intmax_t wcstoimax(const wchar_t *restrict nptr, wchar_t **restrict endptr,
                      int base);
    uintmax_t wcstoumax(const wchar_t *restrict nptr, wchar_t **restrict endptr,
                        int base);

