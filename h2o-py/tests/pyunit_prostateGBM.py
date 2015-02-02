import sys
import h2o

######################################################
#
# Sample Running GBM on prostate.csv

def prostateGBM(**kwargs):
  # Connect to a pre-existing cluster
  h2o.init(kwargs)  # connect to localhost:54321

  df = h2o.import_frame(path="smalldata/logreg/prostate.csv")
  print df.describe()

  # Remove ID from training frame
  train = df.drop("ID")

  # For VOL & GLEASON, a zero really means "missing"
  vol = train['VOL']
  vol[vol == 0] = None
  gle = train['GLEASON']
  gle[gle == 0] = None

  # Convert CAPSULE to a logical factor
  train['CAPSULE'] = train['CAPSULE'].asfactor()

  # See that the data is ready
  print train.describe()

  # Run GBM
  from h2o import H2OGBM

  my_gbm2 = gbm(y=train["CAPSULE"],
                x=range(1, train.ncol(), 1),
                ntrees=50,
                learn_rate=0.1)
  my_gbm2.show()

  my_gbm_metrics2 = my_gbm2.model_performance(train)
  my_gbm_metrics2.show()

  my_gbm_metrics2.show(criterion=my_gbm_metrics2.theCriteria.PRECISION)

if __name__ == "__main__":
  args = sys.argv
  print args
  if len(args) > 1:  prostateGBM(args[1],int(args[2]))
  else:              prostateGBM("localhost",54321)