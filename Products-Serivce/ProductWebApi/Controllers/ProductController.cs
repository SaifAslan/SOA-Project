using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using ProductWebApi.Models;

namespace ProductWebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductController : ControllerBase
    {
        private readonly ProductDbContext _productDbContext;
        public ProductController(ProductDbContext productDbContext) 
        { 
            _productDbContext = productDbContext;
        }
        [HttpGet]
        public ActionResult<IEnumerable<Product>> GetProducts()
        {
            return _productDbContext.Products;
        }
        [HttpGet("{productId:int}")]
        public async Task<ActionResult<Product>> GetById(int productId)
        {
            var product = await _productDbContext.Products.FindAsync(productId);
            return product;
        }
        [HttpPost]
        public async Task<ActionResult> Create(Product product)
        {
            await _productDbContext.Products.AddAsync(product);
            //saves db changes
            await _productDbContext.SaveChangesAsync();
            return Ok();

        }
        //Updates existing record
        //excepts product object as a parameter
        [HttpPut]
        public async Task<ActionResult> Update(Product product)
        {
            _productDbContext.Products.Update(product);
            await _productDbContext.SaveChangesAsync();
            return Ok(product);
        }
        [HttpDelete("{productId:int}")]
        public async Task<ActionResult> Delete(int productId)
        {
            var product = await _productDbContext.Products.FindAsync(productId);
            _productDbContext.Products.Remove(product);
            await _productDbContext.SaveChangesAsync();
            return Ok();
        }


    }
}
