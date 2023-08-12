using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using ProductWebApi.Models;

namespace ProductWebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductItemController : ControllerBase
    {
        private readonly ProductDbContext _productDbContext;
        public ProductItemController(ProductDbContext productDbContext)
        {
            _productDbContext = productDbContext;
        }
        [HttpGet]
        public ActionResult<IEnumerable<ProductItem>> GetProductItems()
        {
            return _productDbContext.ProductItems;
        }
        [HttpGet("{productItemId:int}")]
        public async Task<ActionResult<ProductItem>> GetById(int productItemId)
        {
            var productItem = await _productDbContext.ProductItems.FindAsync(productItemId);
            return productItem;
        }
        [HttpPost]
        public async Task<ActionResult> Create(ProductItem productItem)
        {
            await _productDbContext.ProductItems.AddAsync(productItem);
            //saves db changes
            await _productDbContext.SaveChangesAsync();
            return Ok();

        }
        //Updates existing record
        //excepts product object as a parameter
        [HttpPut]
        public async Task<ActionResult> Update(ProductItem productItem)
        {
            _productDbContext.ProductItems.Update(productItem);
            await _productDbContext.SaveChangesAsync();
            return Ok(productItem);
        }
        [HttpDelete("{productItemId:int}")]
        public async Task<ActionResult> Delete(int productItemId)
        {
            var productItems = await _productDbContext.ProductItems.FindAsync(productItemId);
            _productDbContext.ProductItems.Remove(productItems);
            await _productDbContext.SaveChangesAsync();
            return Ok();
        }
    }
}
