
import os
from configparser import ConfigParser
#from reframed import set_default_solver
#from reframed.solvers.solver import default_parameters, Parameter

__version__ = '1.6.2'

project_dir = os.path.abspath(os.path.dirname(__file__)) + '/'

config = ConfigParser()
config.read(project_dir + 'config.cfg')
for k,v in config.items():
    if os.pathsep in v:
        if not os.path.exists(v):
            raise ValueError(f'file {v} not found')

#set_default_solver(config.get('solver', 'default_solver'))
#default_parameters[Parameter.FEASIBILITY_TOL] = config.getfloat('solver', 'feas_tol')
#default_parameters[Parameter.OPTIMALITY_TOL] = config.getfloat('solver', 'opt_tol')
#default_parameters[Parameter.INT_FEASIBILITY_TOL] = config.getfloat('solver', 'int_feas_tol')
