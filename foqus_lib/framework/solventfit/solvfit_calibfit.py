import subprocess

# ---------------------------------------
# SOLVENTFIT CALIBRATION fit function
# ---------------------------------------
def fit(nx_design, nx_var, xdatfile, ydatfile, modelfile, expfile, priorsfile, disc=True, writepost=True, writedisc=True,
        emul_params=None, calib_params=None, disc_params=None):
    if emul_params is None:
        emul_params = {'bte':'[0,1000,1]',
                      'nterms':'20',
                      'order':'2'}
    if calib_params is None:
        calib_params = {'bte': '[0,1000,1]'}

    booldict = {True:'1', False:'0'}
    disc = booldict[disc]
    writepost = booldict[writepost]
    writedisc = booldict[writedisc]

    if disc_params is None:
        disc_params = {'nterms':'20',
                       'order':'2'}

    p = subprocess.Popen(['Rscript', 'solvfit_calibfit.R',
                          nx_design, nx_var, xdatfile, ydatfile, modelfile,
                          expfile, priorsfile, disc, writepost, writedisc,
                          emul_params['bte'], emul_params['nterms'], emul_params['order'],
                          calib_params['bte'], disc_params['nterms'], disc_params['order']],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)

    return modelfile

# ---------------------------------------
# Example usage
# ---------------------------------------
rdsfile = fit('1','3','example/xdat.csv','example/ydat.csv','solvfit_calibrator.rds',
              'example/expdat1.csv','example/priors.txt', disc=True)
print(rdsfile)
