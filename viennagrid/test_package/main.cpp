#include <iostream>

#include "viennagrid/forwards.hpp"
#include "viennagrid/config/default_configs.hpp"
#include "viennagrid/mesh/mesh.hpp"

using MeshType = viennagrid::triangular_2d_mesh;
using std::cout;
using std::endl;

int main(int argc, char** argv)
{
  MeshType mesh;

  cout << "mesh object created" << endl;

}
