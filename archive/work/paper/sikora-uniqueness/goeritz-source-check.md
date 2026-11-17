# Goeritz presentation: exact source check

**Verdict.** The required statement holds for every nonempty link, including split links and determinant zero. No nonsplit, alternating, or nonzero-determinant hypothesis is needed.

The exact source is W. B. Raymond Lickorish, *An Introduction to Knot Theory*, Graduate Texts in Mathematics 175, Springer-Verlag, New York, 1997, Chapter 9:

- Theorem 9.3, printed p. 96: a matrix of the Gordon–Litherland form of a connected spanning surface of a link presents the first integral homology of its double branched cover.
- The definition on printed p. 98 explicitly assumes a connected diagram and obtains the Goeritz matrix by deleting one row and the corresponding column from the pre-Goeritz matrix.
- Theorem 9.4, printed p. 99: this reduced matrix represents the form of the checkerboard spanning surface.
- Corollary 9.5, printed p. 99: the absolute determinant of this matrix is the link determinant.

[Publisher chapter, pp. 93–102](https://doi.org/10.1007/978-1-4612-0691-0_9).

## Suggested manuscript wording

~~~latex
Choose a connected diagram of \(L\); even for a split link this can
be achieved by planar isotopies and Reidemeister~II moves joining
the components of its projection. Let \(G\) be a reduced Goeritz
matrix of this diagram. By
\cite[Theorems~9.3--9.4 and Corollary~9.5]{LickorishBook},
\[
 H_1(\Sigma_2(L);\Z)\cong\operatorname{coker}G,
 \qquad \Det L=|\det G|.
\]
Smith normal form therefore gives order \(|\det G|\) when
\(\det G\ne0\), and a nonzero free summand when \(\det G=0\).
Thus \(h(\Sigma_2(L))=\Det L\), including determinant zero
and split links.
~~~

The independent last step is elementary: a singular square integer matrix has positive rational corank, so its cokernel has positive free rank. Adding a Reidemeister II pair connects two components of the planar projection without changing the represented link; repeating gives the required connected diagram. Its checkerboard surface is connected, making Theorem 9.3 applicable.

## Bibliography entry

~~~latex
\bibitem{LickorishBook}
W.~B.~Raymond Lickorish,
\emph{An introduction to knot theory},
Graduate Texts in Mathematics, vol.~175,
Springer-Verlag, New York, 1997.
\href{https://doi.org/10.1007/978-1-4612-0691-0}
{doi:10.1007/978-1-4612-0691-0}.
~~~

## Verification record

The publisher chapter metadata and abstract were opened. The numbered statements, connected-diagram definition, and surrounding proofs on the original printed pages were read through search-index extraction of the scanned book, rather than inferred from another paper's citations. Opening the full scan exceeded the web tool's size limit; the publisher chapter PDF resolved to its subscription page. The theorem content was directly checked in original-text extraction, with that access limitation.
