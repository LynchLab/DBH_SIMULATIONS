Addressing Reviewer 2's concerns.

These are a small number of scripts which generated the figures presented later in this document. This document is intended to demonstrate the basic validity of the analysis performed in Sung et al 2012 and in Sung et al 2016. In these papers we looked for a correlation between effective population size (Ne), which is a measure of the power of drift, and the per generation deleterious mutation rate (U). In Sung et al 2012 we examined the per base pair mutation rate (mu\_bp), and in Sung et al. 2016 we examined the indel mutation rate (mu\_id).  

Because the per generation deleterious mutation rate is the phenotype most directly exposed to selection, and because as deleterious mutation rates become small the benefits of decreasing the deleterious mutation rate further diminish, and finally because effective population size determines the minimum benefit which selection can effectively favor, we expected to see a negative correlation between (U) and effective population size(Ne). However, we do not measure either of these variables directly. Instead effective population size is calculated as the ratio of silent site diversity (pi) and the per base pair mutation rate (Ne=pi/mu\_bp). Additionally the deleterious mutation rate is calculated as the product of effective genome size (Ge) and the per base pair mutation rate (U\_bp=Ge\*mu\_bp) or the indel mutation rate (U\_id=Ge\*mu\_id) . To test for this relationship we look for a correlation between the logarithm of Ne and logarithm of U. Concerns are often expressed to us verbally that there is something fishy about looking for a correlation between Ge\*mu and pi/mu, since the mutation rate occurs in both terms. We address this concern by discussing the statistical properties of the null hypothesis, which is not that the variables which we measure (pi, mu and Ge) are uncorrelated. Additionally, this discussion allows us to derive an exact expression for the effect of error in the measurement of mu\_bp and mu\_id on the correlations we observe. 

For the null hypothesis to be true (that deleterious mutation rates and effective population size are uncorrelated), some of the parameters we measure (pi, mu and Ge) must be correlated (except in a trivial case where mu is constant). This is true because Cov(Ud, Ne)=0 implies that Cov(Ge+mu, pi-mu)=Cov(Ge, pi)-cov(Ge, mu)+cov(pi, mu)-var(mu)=0. Since var(mu) is strictly positive some of the covariance terms must be non zero. If we assume that the effective population size is uncorrelated with the per base pair mutation rate, Cov(Ne, mu), then we get that Cov(pi, mu)=var(mu), and we can safely assume that Cov(Ge, pi)=0 and Cov(Ge, mu)=0 while maintaining the independence of the deleterious mutation rate and effective population sizes. Under these assumptions there will be a correlation between the per genome deleterious mutation rate and the per base pair mutation rate and  a correlation between silent site diversity and the per base pair mutation rate. Both of these correlations seem biologically reasonable, since silent site diversity measures the ratio of the power of drift and the power of mutation, if effective population size remains constant as mutation rate increases, then there will be a corresponding increase in silent site diversity.

In order to test the null hypothesis we ask whether: Cov(Ge, mu) and Cov(Ge, pi) are both 0, and whether Cov(pi, mu)=var(mu). One of the peculiarities of this test is that we expect a particular nonzero relationship between Cov(pi, mu) and var(mu). We wish to take the observation that Cov(pi, mu) is less than var(mu) as support for the drift barrier hypothesis. There is nothing intrinsically wrong with this approach, however, we do have to be wary of possibility that measurement error has decreased the expected covariance of pi and mu, since the error in our measurement of mu will be uncorrelated with the pi, even though mu itself is correlated with pi. This problem can be dealt with by assessing the magnitude of measurement error necessary to diminish the covariance of pi and mu to a significant extent. ...

Finally let's turn to the drift barrier hypothesis itself. As stated previously, if the drift barrier hypothesis is correct, we should see a relationship between Ne and U. This directly implies a negative correlation between Ge and pi. The drift barrier hypothesis makes no direct prediction of a relationship between mu and pi; however, it is plausible that Ne might have some effect on effective genome size, which would create an indirect relationship between Ne and pi of similar magnitude and opposite sign. Alternatively it is possible that pi systematically underestimates Ne whenever pi is large. This would create a negative relationship between mu and pi, but would create no corresponding relationship between Ge and mu, since it would reflect an error in our estimation of Ne, and not a fundamental biological phenomenon.  

As seen in figure S1a, the magnitude of the measurements error which would be necessary to achieve our results if the null hypothesis were true is profound. Additionally, this error would need to be highly correlated between measurements of base substitution rate and indel rate (figure S1b). While there is likely some correlation between error of these measurements, since they both are influenced by sequencing depth, our measurements of the mutation rate would have to be essentially uncorrelated with actual mutation rates (figure S2) to explain the observations, if the null hypothesis were true. 

Finally, one of the predictions of the drift barrier hypothesis is that effective genome size and silent site diversity should be correlated. This prediction is appealing in that it should be true independent of the mutation rate. Measurement errors in mutation rates, no matter how profound, could not effect this signal. We see this correlation in our data (Figure S3 and Table S1).

Figure S1: The correlation between Ne and U under the null hypothesis, as a function of error.

![Figure S1](https://github.com/LynchLab/DBH_SIMULATIONS/figureS1.jpg)

Figure S2:
![Figure S2](https://github.com/LynchLab/DBH_SIMULATIONS/figureS2.jpg)

Figure S3: The correlation between actual and measured mutation rates, as a function of error.
![Figure S3](https://github.com/LynchLab/DBH_SIMULATIONS/figureS3.jpg)

Figure S4: The correlation between pi and Ge
![Figure S4](https://github.com/LynchLab/DBH_SIMULATIONS/figureS4.jpg)

Table 1:

| Cov	|     slope	 | Null  | DBH  | DBH+G   | DBH+s|
|-------|----------------|-------|------|---------|------|
|Ge, u	| (-0.40, 0.43)	 | 0     |  0   | +/-0.5  |  0   |
|Ge, pi	| (-1.35, -0.32) | 0\*   | -1   |  -1     | -1   |
| u, pi	| (-1.33, -0.02) | 1\*\* | 0\*  | -/+0.5  | -b   |

