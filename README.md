# Molecular Evolution Tutorial
Tutorial for BIOL 6210 (Applied Pylogentics)
### Installing PAML (macosx)

```bash
curl http://abacus.gene.ucl.ac.uk/software/paml4.8a.macosx.tgz > paml4.8a.macosx.tgz
tar -xvzf paml4.8a.macosx.tgz
cd paml4.8
rm bin/*.exe
cd src
make -f Makefile
ls -lF
rm *.o
mv baseml basemlg codeml pamp evolver yn00 chi2 ../bin
cd ..
ls -lF bin
export PATH=$PATH:bin
```

See http://abacus.gene.ucl.ac.uk/software/paml.html for **Windows** installation instructions.



##All the files needed for this tutorial are located  **[here](https://drive.google.com/file/d/0ByIk6IH2yiS0eWhQLWRVT3pBdTQ/view?usp=sharing)**

## Identification of positive seleciton in the serine/threonine-protein kinase gene family

* In the evolution vertebrates, we would like to know if the branch leading to the Teleost fishes (genes A50 to A54)


You will need the following files

**1. TF105351.Eut.3.phy**<br>
* this is the alignment file

![alt tag](https://3.bp.blogspot.com/-LxFevYQBQ7I/TnN0vARVO4I/AAAAAAAAABM/PAxYkWUTQcw/s320/TF105351.Eut.3.aln.png)

**2. TF105351.Eut.3.53876.tree**
* this is the newick tree with the branch of interest selected

![alt tag](https://2.bp.blogspot.com/-QCyFGC6o2zQ/Uad84nz-S3I/AAAAAAAAAEg/W12U2V0CizQ/s1600/Tree.png)

**3. TF105351.Eut.3.53876.ctl**
* CodeML configuration file for ___alternative model___

**4. TF105351.Eut.3.53876.fixed.ctl**
* CodeML configuration file for ___null model___

### Run the following commands
```bash
codeml TF105351.Eut.3.53876.ctl
codeml TF105351.Eut.3.53876.fixed.ctl
```

### Analyze results
Get liklihood values
```
grep lnL TF105351.Eut.3.53876.mlc
```

```
lnL(ntime: 41  np: 46):  -4707.209701      +0.000000
```

Liklihood value for alternative model is **-4707.209701**

```
grep lnL TF105351.Eut.3.53876.fixed.mlc
```
```
lnL(ntime: 41  np: 45):  -4710.222252      +0.000000
```
Liklihood value for null model is **-4710.222252**

ΔLRT = 2×(lnL1 - lnL0) = 2×(-4707.209701 - (-4710.222252)) = 6.02578

The degree of freedom is 1 (np1 - np0 = 46 - 45).
p-value = 0.01098 (under χ²) => significant.
