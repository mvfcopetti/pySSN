'''
Created on 17/01/2014

@author: morisset
'''
#-------------------------------------------------------------------
#   Initialisation
#-------------------------------------------------------------------

log_level = 3
#
# All the following variables (most of them boolean) can be
# set here, or in the init_file of the model you are doing,
# or interactively at the X-SSN prompt or sometime in the 
# control panel.
#
   
# If you want to make a synthesis, let it to 1.
# Set it to 0 if you don't want to make a synthesis 
# (changing only the continuum, the redening, Raman for exemple)
do_synth = 1

# If you want to read the liste of lines, let it to 1.
# Set it to 0 if you just want to run a new synthesis with 
# the same lines (modification of the profiles, lambda-calibration...)
# Note that if do_synth = 0, the following flag has no meaning. 
do_read_liste = 1

# If you want to plot the results of the synthesis, let it to 1
do_plot_results = 1

# If you want to overplot the Raman components, let it to 1
do_plot_raman =  0
   
# If you want to plot the theoretical spectra, let it to 1 (and see after)
do_plot_multi = 0

# If you want to plot the calibration, let it to 1.
plot_calib = 0

# Here is the limite of the intergrated intensity of the theoretical
# spectra to be plotted.
lim_plot_multi_synth = 1.

# If you DON'T want an i_cor on a main line to affect the satellites, 
# set the following variable to 0
recursive_i_cor = 1

# Is i_cor applied in the atomic physic database AND model database?
# If this is the case, i_cor on phyat_database will be directly
# applied on i_rel and will not appear as i_cor in the printed liste
# of lines or with the cursor.
do_icor_outside_cosmetik = 1

# If you want to perform cosmetik on reference lines (which have ref = 0):
do_icor_on_ref = 1

# Wanna be sure that the listes of lines are correct? set to 1 
do_debug_liste = 0
warn_on_no_cosmetik = True
warn_on_no_reference = True

# Factor applied to the observations
sp_norm = 1.0

# Applied to the synthese
lambda_shift = 0.0 # w units

spectr_obs = None 
sp_norm = 1.0 #  
lambda_pix = 0.1 #
limit_sp = [0, 1.0e+10]
# Velocity of the object, applied to the wavelengths in the
# calibration of the observations

obj_velo = 0. # km/s

# If data are in fits format, set it to 1
data_is_fits = 0

# If data are in xdr format, set it to 1
data_is_xdr = 0

# If observed spectra is to be reversed to let the wavelength growing
reverse_spectra = 1

# If the data include the wavelengths (1st column), set the following to 1
data_incl_w =  0

# if wavelength calibration needed, set to 1:
do_calib =  1         # necessarily = 1 in case data_incl_w =  0

# Here are the 2 filenames of the data. The filename 
# of the atomic database is hard-coded (in read_liste.pro)
fic_cosmetik = 'liste_cosmetik.dat'
fic_modele = 'liste_modele.dat'


# Atmospheric lines in the following files:
fic_atm = None
coeff_atm = 0.0
shift_atm = 0.0

# Here is the format of the listes

##25/9/9 format_liste = '(i9,a12,f9.3,f6.3,e10.3,f7.3,1x,i9,1x,i3,1x,f6.2,a25)'
# format_liste = '(i9,a10,f11.3,f6.3,e10.3,f7.3,1x,i9,1x,i3,1x,f6.2,a25)'
format_liste = '(i14,a10,f11.3,f6.3,e10.3,f7.3,1x,i14,1x,i3,1x,f6.2,a25)'

# Here follow caracteristics of the reference line.
# This line will be assumed to have a flux
# at center of 1.00/A. 

do_calcul_aire_ref = 0  
raie_ref =  {"vitesse" : 25.0, "lambda" : 4861.0, "profile" : 1}      # depuis 25/10/01

# Here is the name of the function used for the emission profiles:
profil_emis_name = 'profil_emis'

# Index number of the balmer line in the spectrum, for the Raman
# diffusion.
num_Balmer = [0]    # Alpha = 0, Beta = 1, ...

# Velocities and Intensities of the Raman scattering components
raman_velocity = [-0.0,  19.0,  50.] 
intens_raman =  [[.0],[0.],[.00]]  # 0.25  1 comp
#
#
# If limit_sp is undefined, then the computing interval is
# the observed one increased by delta_limit_sp at
# each side.
#
delta_limit_sp =  10.

#
# Rebinning factor applied to the observations before the synthesis.
# Nouveau mode.
resol = 1  # Resol must be small if the obs resol is large

# Resol should be odd (otherwise, 1 will be automatically added).
# If you change this, verify that all the
# lines with the same profile have the same area
# Look at make_synth.pro, there is a line to uncomment to get 
# the list of the areas of the lines.
# Will be replaced by Resol (as soon as the bug is fixed...)
high_resolution = 1

# initialisation of the continuum flux 
cont_in_lambda = 0 #set to 1 if the continuum is in wavelength
cont_unred = 1 #set to 1 if redeening is to be applied to cont
cont_lambda = 0.
cont_pix = 0
cont_intens = 0.
cont_bb_t = 11000.
cont_bb_i = 0.
cont_pl_alpha = 1.
cont_pl_i = 0.
cont_ihi = 1.e4
cont_ihei = 3.e2
cont_iheii = 0.e3
cont_Thi = 1e4
cont_Thei = 1e4
cont_Theii = 1e4
cont_edens = 1e3

# Wavelength of the reference line for the reddening.
lambda_ref_rougi = 4861.3
red_corr_law = 'S79 H83 CCM89'

# definition of the structure for the limits of the plots
x_plot_lims = (limit_sp[0],limit_sp[1])
y1_plot_lims = None
y2_plot_lims = (-1.5, 1.)
y3_plot_lims = None

# Color lines
plot_magenta = None
label_magenta = ''
plot_cyan = None
label_cyan = ''

# Plot the second and third panels
plot_ax2 = True
plot_ax3 = True

# Scale factor for the plot of the theoretical (individual) spectra:
fact_multi_synth =  1.

# If you want to print eps file, set it to 1:
print_eps = 0

# ticks will appear for lines with theoretical intensity >/= cut value
# is also used in the printed list of lines
cut_affich_lines = 0.
cut_o_affich_lines = 0.

# norm_intens: value by which are divided the line intensities in
# the printed table
norm_intens = 1.00e4

line_select = 0

verbose = 1


# instrument
prof = {'largeur':0.50,
    'B_1r':0.00,'B_1l':0.00,'decroiss_1':2.70,'alpha_1':0.50,
    'B_2r':0.00,'B_2l':0.00,'decroiss_2':1.50,'alpha_2':0.75,
    'B_3r':0.00,'B_3l':0.00,'decroiss_3':1.15,'alpha_3':1.00,
    'B_4r':0.00,'B_4l':0.00,'decroiss_4':0.45,'alpha_4':1.50,
    'comment':' Gauss'   }

ghost =  {"do_ghost":0, "delta_lambda" : 0. , "intens" : [ 0.00]}

#ghost =  {do_ghost:1, $
#          delta_lambda : [2.74,-2.75,5.2,-5.2] , $
#          largeur : [0.5,0.5,0.7,0.7],$
#          intens : [ 0.00310000, $
#                      0.000880000, $
#                      3.50000e-05, $
#                      8.00000e-06] }

