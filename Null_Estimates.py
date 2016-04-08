import numpy

print "cor_id_bp, cor_mu_psudo, corr_Ne_U"

for X in range (1, 100):
	x=float(X)/100
	z=1.0
	psudo_ud=[]
	psudo_ne=[]
	for Q in range (0, 1000):
		[mean_Ne, var_Ne]=[2.35,9.36]
	#	[mean_Ud, var_Ud]=[2.55,9.22]
		[mean_mu, var_mu]=[1.99,3.92]
		[mean_Ge, var_Ge]=[0.56,3.17]

		Ne=numpy.random.normal(mean_Ne, var_Ne)	# The real effective population size in the null model.
	#	Ud=numpy.random.normal(mean_Ud, var_Ud)	# The real deleterious mutation rate in the null model.
		cov=[ [var_mu,var_mu*x,var_mu*x],[var_mu*x,var_mu,var_mu*z],[var_mu*x,var_mu*z,var_mu] ]
		[mu, psudo_mu1, psudo_mu2]=numpy.random.multivariate_normal( (mean_mu, mean_mu, mean_mu), cov)	# The real per base pair mutation rate in the null model.
		Ge=numpy.random.normal(mean_Ge, var_Ge)	# The real per base pair mutation rate in the null model.

#		print mu, psudo_mu1, psudo_mu2

		Ud=Ge+mu
		pi=Ne+mu				# The real silent site diversity in the null model.
	#	Ge=Ud-mu				# The real effective genome size in the null model.
	#	var=19.69

		pi_err=0#numpy.random.normal(0, var)	#Our simulate measurement errors.
		Ge_err=0#numpy.random.normal(0, var)	#	"	"

		psudo_Ge=Ge
		psudo_pi=pi

		psudo_ud.append(psudo_Ge+psudo_mu1)	#Our simulated deleterious mutation rate. 
		psudo_ne.append(psudo_pi-psudo_mu2)	#Our simulated effective population size.
	print z, x, numpy.corrcoef(psudo_ud, psudo_ne)[0][1]
#	print Ne, Ud, mu, pi, Ge, psudo_mu, psudo_pi, psudo_Ge, psudo_ne, psudo_ud

for Z in range (1, 100):
	x=1.0
	z=float(Z)/100
	psudo_ud=[]
	psudo_ne=[]
	for Q in range (0, 1000):
		[mean_Ne, var_Ne]=[2.35,9.36]
	#	[mean_Ud, var_Ud]=[2.55,9.22]
		[mean_mu, var_mu]=[1.99,3.92]
		[mean_Ge, var_Ge]=[0.56,3.17]

		Ne=numpy.random.normal(mean_Ne, var_Ne)	# The real effective population size in the null model.
	#	Ud=numpy.random.normal(mean_Ud, var_Ud)	# The real deleterious mutation rate in the null model.
		cov=[ [var_mu,var_mu*x,var_mu*x],[var_mu*x,var_mu,var_mu*z],[var_mu*x,var_mu*z,var_mu] ]
		[mu, psudo_mu1, psudo_mu2]=numpy.random.multivariate_normal( (mean_mu, mean_mu, mean_mu), cov)	# The real per base pair mutation rate in the null model.
		Ge=numpy.random.normal(mean_Ge, var_Ge)	# The real per base pair mutation rate in the null model.

		Ud=Ge+mu
		pi=Ne+mu				# The real silent site diversity in the null model.
	#	Ge=Ud-mu				# The real effective genome size in the null model.
	#	var=19.69

		pi_err=0#numpy.random.normal(0, var)	#Our simulate measurement errors.
		Ge_err=0#numpy.random.normal(0, var)	#	"	"

		psudo_Ge=Ge
		psudo_pi=pi

		psudo_ud.append(psudo_Ge+psudo_mu1)	#Our simulated deleterious mutation rate. 
		psudo_ne.append(psudo_pi-psudo_mu2)	#Our simulated effective population size.
	print z, x, numpy.corrcoef(psudo_ud, psudo_ne)[0][1]
#	print Ne, Ud, mu, pi, Ge, psudo_mu, psudo_pi, psudo_Ge, psudo_ne, psudo_ud
