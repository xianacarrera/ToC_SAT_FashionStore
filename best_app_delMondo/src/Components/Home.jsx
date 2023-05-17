
import character from './Character.png'

const Home = () => {

    const dummy_function = (obj) => {
        console.log(obj)
    }
    
    return (

        <div className="grid grid-cols-5  gap-5">
            <div>01</div>
            <div className="col-span-3 flex justify-center items-center" ><img src={character} className=" object-center h-screen" alt="logo" /></div>
            <div>01</div>
        </div>
    )


}
export default Home