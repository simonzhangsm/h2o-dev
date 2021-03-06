import sys
sys.path.insert(1, "../../../")
import h2o

def cupMediumGBM(ip,port):
  # Connect to h2o
  h2o.init(ip,port)
  
  train = h2o.import_frame(path=h2o.locate("bigdata/laptop/usecases/cup98LRN_z.csv"))
  test = h2o.import_frame(path=h2o.locate("bigdata/laptop/usecases/cup98VAL_z.csv"))
  
  # Train H2O GBM Model:
  train_cols = train.names()
  for c in ['', "TARGET_D", "TARGET_B", "CONTROLN"]:
    train_cols.remove(c)
  model = h2o.gbm(x=train[train_cols], y=train["TARGET_B"], loss = "AUTO", ntrees = 5)

if __name__ == "__main__":
  h2o.run_test(sys.argv, cupMediumGBM)
