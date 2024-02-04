import { Stack, Flex, Button, Text, VStack, useBreakpointValue } from '@chakra-ui/react'
import { Link } from 'react-router-dom'

export default function LandingPage() {
  return (
    <Flex
      w={'full'}
      h={'100vh'}
      backgroundImage={
        'url(https://images.pexels.com/photos/93398/pexels-photo-93398.jpeg)'
      }
      backgroundSize={'cover'}
      backgroundPosition={'center center'}>
      <VStack
        w={'full'}
        justify={'center'}
        px={useBreakpointValue({ base: 4, md: 8 })}
        bgGradient={'linear(to-r, blackAlpha.600, transparent)'}>
        <Stack maxW={'2xl'} align={'flex-start'} spacing={6}>
          <Text
            color={'white'}
            fontWeight={700}
            lineHeight={1.2}
            fontSize={useBreakpointValue({ base: '3xl', md: '4xl' })}>
            As much as we love amazon prime, we need to look out for how much carbon footprint our shopping habits lead to.  
          </Text>
          <Stack direction={'row'}>
            <Link to={"search"}>
            <Button
              bg={'blue.400'}
              rounded={'full'}
              color={'white'}
              size={"lg"}
              _hover={{ bg: 'blue.500' }}>
              Show me 
            </Button>
            </Link>
          </Stack>
        </Stack>
      </VStack>
    </Flex>
  )
}