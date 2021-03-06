package hex.schemas;

import hex.kmeans.KMeans;
import hex.kmeans.KMeansModel.KMeansParameters;
import water.api.API;
import water.api.ClusteringModelParametersSchema;
import water.api.KeyV1;
import water.api.ModelParametersSchema;
import water.fvec.Frame;

public class KMeansV2 extends ClusteringModelBuilderSchema<KMeans,KMeansV2,KMeansV2.KMeansParametersV2> {

  public static final class KMeansParametersV2 extends ClusteringModelParametersSchema<KMeansParameters, KMeansParametersV2> {
    static public String[] own_fields = new String[] { "user_points", "max_iterations", "standardize", "seed", "init" };

    // Input fields
    @API(help = "User-specified points", required = false)
    public KeyV1.FrameKeyV1 user_points;

    @API(help="Maximum training iterations")
    public int max_iterations;        // Max iterations

    @API(help = "Standardize columns", level = API.Level.secondary)
    public boolean standardize = true;

    @API(help = "RNG Seed", level = API.Level.expert /* tested, works: , dependsOn = {"k", "max_iterations"} */ )
    public long seed;

    @API(help = "Initialization mode", values = { "Random", "PlusPlus", "Furthest", "User" }) // TODO: pull out of enum class. . .
    public KMeans.Initialization init;
  }
}
